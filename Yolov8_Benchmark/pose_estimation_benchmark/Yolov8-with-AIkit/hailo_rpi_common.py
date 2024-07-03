import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib
import os
import argparse
import multiprocessing
import numpy as np
import setproctitle
import cv2
import time

# Try to import hailo python module
try:
    import hailo
except ImportError:
    exit("Failed to import hailo python module. Make sure you are in hailo virtual environment.")
from hailo_common_funcs import get_numpy_from_buffer, disable_qos

# -----------------------------------------------------------------------------------------------
# User defined class to be used in the callback function
# -----------------------------------------------------------------------------------------------
# a sample class to be used in the callback function
# This example allows to:
# 1. count the number of frames
# 2. Setup a multiprocessing queue to pass the frame to the main thread
# Additional variables and functions can be added to this class as needed

class app_callback_class:
    def __init__(self):
        self.frame_count = 0
        self.use_frame = False
        self.frame_queue = multiprocessing.Queue(maxsize=3)
        self.running = True

    def increment(self):
        self.frame_count += 1

    def get_count(self):
        return self.frame_count 

    def set_frame(self, frame):
        if not self.frame_queue.full():
            self.frame_queue.put(frame)
        
    def get_frame(self):
        if not self.frame_queue.empty():
            return self.frame_queue.get()
        else:
            return None

# -----------------------------------------------------------------------------------------------
# Common functions
# -----------------------------------------------------------------------------------------------
def get_caps_from_pad(pad: Gst.Pad):
        caps = pad.get_current_caps()
        if caps:
            # We can now extract information from the caps
            structure = caps.get_structure(0)
            if structure:
                # Extracting some common properties
                format = structure.get_value('format')
                width = structure.get_value('width')
                height = structure.get_value('height')
                # string_to_print += (f"Frame format: {format}, width: {width}, height: {height}\n")
                return format, width, height
        else:
            return None, None, None

# This function is used to display the user data frame
def display_user_data_frame(user_data: app_callback_class):
    while user_data.running:
        frame = user_data.get_frame()
        if frame is not None:
            cv2.imshow("User Frame", frame)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    
def get_default_parser():
    parser = argparse.ArgumentParser(description="Hailo App Help")
    parser.add_argument("--input", "-i", type=str, default="/dev/video0", help="Input source. Can be a file, USB or RPi camera (CSI camera module). \
                        For RPi camera use '-i rpi' (Still in Beta). \
                        Defaults to /dev/video0")
    parser.add_argument("--use-frame", "-u", action="store_true", help="Use frame from the callback function")
    parser.add_argument("--show-fps", "-f", action="store_true", help="Print FPS on sink")
    parser.add_argument("--disable-sync", action="store_true", help="Disables display sink sync, will run as fast possible. Relevant when using file source.")
    parser.add_argument("--dump-dot", action="store_true", help="Dump the pipeline graph to a dot file pipeline.dot")
    return parser


def QUEUE(name, max_size_buffers=3, max_size_bytes=0, max_size_time=0):
    return f"queue name={name} max-size-buffers={max_size_buffers} max-size-bytes={max_size_bytes} max-size-time={max_size_time} ! "

def get_source_type(input_source):
    # This function will return the source type based on the input source
    # return values can be "file", "mipi" or "usb"
    if input_source.startswith("/dev/video"):
        return 'usb'
    else:
        if input_source.startswith("rpi"):
            return 'rpi'
        else:
            return 'file'

# -----------------------------------------------------------------------------------------------
# GStreamerApp class
# -----------------------------------------------------------------------------------------------
class GStreamerApp:
    def __init__(self, args, user_data: app_callback_class):
        # Set the process title
        setproctitle.setproctitle("Hailo Python App")
        
        # Create an empty options menu
        self.options_menu = args
        
        # Initialize variables
        tappas_postprocess_dir = os.environ.get('TAPPAS_POST_PROC_DIR', '')
        if tappas_postprocess_dir == '':
            print("TAPPAS_POST_PROC_DIR environment variable is not set. Please set it to by sourcing setup_env.sh")
            exit(1)
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.postprocess_dir = tappas_postprocess_dir
        self.video_source = self.options_menu.input
        self.source_type = get_source_type(self.video_source)
        self.user_data = user_data
        self.video_sink = "xvimagesink"
        
        # Set Hailo parameters these parameters shuold be set based on the model used
        self.batch_size = 1
        self.network_width = 640
        self.network_height = 640
        self.network_format = "RGB"
        self.default_postprocess_so = None
        self.hef_path = None
        self.app_callback = None

        # Set user data parameters
        user_data.use_frame = self.options_menu.use_frame

        if (self.options_menu.disable_sync or self.source_type != "file"):
            self.sync = "false" 
        else:
            self.sync = "true"
        
        if (self.options_menu.dump_dot):
            os.environ["GST_DEBUG_DUMP_DOT_DIR"] = self.current_path
    
    def on_fps_measurement(self, sink, fps, droprate, avgfps):
        print(f"FPS: {fps:.2f}, Droprate: {droprate:.2f}, Avg FPS: {avgfps:.2f}")
        return True

    def create_pipeline(self):
        # Initialize GStreamer
        Gst.init(None)
        
        pipeline_string = self.get_pipeline_string()
        try:
            self.pipeline = Gst.parse_launch(pipeline_string)
        except Exception as e:
            print(e)
            print(pipeline_string)
            exit(1)
        
        # connect to hailo_display fps-measurements
        if (self.options_menu.show_fps):
            print("Showing FPS")
            self.pipeline.get_by_name("hailo_display").connect("fps-measurements", self.on_fps_measurement)

        # Create a GLib Main Loop
        self.loop = GLib.MainLoop()
        
    def bus_call(self, bus, message, loop):
        t = message.type
        if t == Gst.MessageType.EOS:
            print("End-of-stream")
            loop.quit()
        elif t == Gst.MessageType.ERROR:
            err, debug = message.parse_error()
            print(f"Error: {err}, {debug}")
            loop.quit()
        # QOS
        elif t == Gst.MessageType.QOS:
            # Handle QoS message here
            qos_element = message.src.get_name()
            print(f"QoS message received from {qos_element}")
        return True
    
    
    def get_pipeline_string(self):
        # this is a placeholder function that should be overridden by the child class
        return ""
    
    def dump_dot_file(self):
        print("Dumping dot file...")
        Gst.debug_bin_to_dot_file(self.pipeline, Gst.DebugGraphDetails.ALL, "pipeline")
        return False
    
    def run(self):

        # Add a watch for messages on the pipeline's bus
        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.bus_call, self.loop)

        # Connect pad probe to the identity element
        identity = self.pipeline.get_by_name("identity_callback")
        if identity is None:
            print("Warning: identity_callback element not found, add <identity name=identity_callback> in your pipeline where you want the callback to be called.")
        else:
            identity_pad = identity.get_static_pad("src")
            identity_pad.add_probe(Gst.PadProbeType.BUFFER, self.app_callback, self.user_data)

        # get xvimagesink element and disable qos
        # xvimagesink is instantiated by fpsdisplaysink
        hailo_display = self.pipeline.get_by_name("hailo_display")
        if hailo_display is None:
            print("Warning: hailo_display element not found, add <fpsdisplaysink name=hailo_display> to your pipeline to support fps display.")
        else:
            xvimagesink = hailo_display.get_by_name("xvimagesink0")
            if xvimagesink is not None:
                xvimagesink.set_property("qos", False)
        
        # Disable QoS to prevent frame drops
        disable_qos(self.pipeline)
        
        # start a sub process to run the display_user_data_frame function
        if (self.options_menu.use_frame):
            display_process = multiprocessing.Process(target=display_user_data_frame, args=(self.user_data,))
            display_process.start()

        # Set pipeline to PLAYING state
        self.pipeline.set_state(Gst.State.PLAYING)
        
        # dump dot file
        if (self.options_menu.dump_dot):
            GLib.timeout_add_seconds(3, self.dump_dot_file)
        
        # Run the GLib event loop
        try:
            self.loop.run()
        except:
            pass

        # Clean up
        self.user_data.running = False
        self.pipeline.set_state(Gst.State.NULL)
        if (self.options_menu.use_frame):
            display_process.terminate()
            display_process.join()