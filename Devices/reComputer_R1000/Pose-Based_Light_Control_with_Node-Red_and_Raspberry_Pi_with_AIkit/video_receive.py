import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
import sys

# Initialize GStreamer and GObject
Gst.init(None)
GObject.threads_init()

class VideoReceiver:
    def __init__(self):
        self.pipeline = Gst.Pipeline()

        # Create elements
        self.udpsrc = Gst.ElementFactory.make("udpsrc", "udpsrc")
        self.udpsrc.set_property("port", 2000)
        self.udpsrc.set_property("caps", Gst.caps_from_string("application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264"))
        
        self.rtph264depay = Gst.ElementFactory.make("rtph264depay", "rtph264depay")
        self.h264parse = Gst.ElementFactory.make("h264parse", "h264parse")
        self.avdec_h264 = Gst.ElementFactory.make("avdec_h264", "avdec_h264")
        
        self.videoconvert = Gst.ElementFactory.make("videoconvert", "videoconvert")
        self.autovideosink = Gst.ElementFactory.make("autovideosink", "autovideosink")

        # Add elements to the pipeline
        self.pipeline.add(self.udpsrc)
        self.pipeline.add(self.rtph264depay)
        self.pipeline.add(self.h264parse)
        self.pipeline.add(self.avdec_h264)
        self.pipeline.add(self.videoconvert)
        self.pipeline.add(self.autovideosink)

        # Link elements
        self.udpsrc.link(self.rtph264depay)
        self.rtph264depay.link(self.h264parse)
        self.h264parse.link(self.avdec_h264)
        self.avdec_h264.link(self.videoconvert)
        self.videoconvert.link(self.autovideosink)

        # Set the pipeline state to playing
        self.pipeline.set_state(Gst.State.PLAYING)

    def run(self):
        # Start the main loop
        loop = GObject.MainLoop()
        try:
            loop.run()
        except KeyboardInterrupt:
            pass
        finally:
            # Clean up
            self.pipeline.set_state(Gst.State.NULL)

if __name__ == "__main__":
    receiver = VideoReceiver()
    receiver.run()
