import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, GLib
import base64
import os
import argparse
import multiprocessing
import numpy as np
import setproctitle
import cv2
import time
import hailo
import paho.mqtt.client as mqtt  # MQTT库
import json

from hailo_rpi_common import (
    get_default_parser,
    QUEUE,
    get_caps_from_pad,
    get_numpy_from_buffer,
    display_user_data_frame,
    GStreamerApp,
    app_callback_class,
)

# Initialize GStreamer
GObject.threads_init()
Gst.init(None)


# MQTT 配置
MQTT_BROKER = "47.119.28.143"  # 替换为你的broker地址
MQTT_PORT = 1883  # MQTT端口
MQTT_TOPIC = "/device/yolo/detections"  # 发布主题
MQTT_USERNAME = "recomputer"  # MQTT用户名
MQTT_PASSWORD = "recomputer"  # MQTT密码


# 初始化MQTT客户端，并设置用户名和密码
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()  # 开启MQTT客户端循环

# 用户定义的回调类
class user_app_callback_class(app_callback_class):
    def __init__(self):
        super().__init__()
        self.use_frame=True

# 用户定义的回调函数
def app_callback(pad, info, user_data):
    buffer = info.get_buffer()  # 从探针信息中获取GstBuffer
    if buffer is None:
        return Gst.PadProbeReturn.OK
    
    user_data.increment()  # 计数帧数
    frame_count = f"{user_data.get_count()}"
    
    format, width, height = get_caps_from_pad(pad)  # 获取视频格式和尺寸信息
    frame = None
    if user_data.use_frame and format is not None and width is not None and height is not None:
        frame = get_numpy_from_buffer(buffer, format, width, height)  # 获取视频帧

    roi = hailo.get_roi_from_buffer(buffer)  # 从缓冲区中获取ROI
    detections = roi.get_objects_typed(hailo.HAILO_DETECTION)  # 获取检测结果
    
    for detection in detections:
        label = detection.get_label()
        bbox = detection.get_bbox()
        confidence = detection.get_confidence()
        if label == "person":  # 仅处理检测到的人
            persion = (f"{label} {confidence:.2f}")
            landmarks = detection.get_objects_typed(hailo.HAILO_LANDMARKS)  # 获取姿态估计关键点
            if len(landmarks) != 0:
                points = landmarks[0].get_points()

                nose = points[0]  # nose
                nose_x = int((nose.x() * bbox.width() + bbox.xmin()) * width)
                nose_y = int((nose.y() * bbox.height() + bbox.ymin()) * height)
                Nose = (f"x: {nose_x:.2f} y: {nose_y:.2f}\n")

                left_eye = points[1]  # 左眼
                right_eye = points[2]  # 右眼
                left_eye_x = int((left_eye.x() * bbox.width() + bbox.xmin()) * width)
                left_eye_y = int((left_eye.y() * bbox.height() + bbox.ymin()) * height)
                right_eye_x = int((right_eye.x() * bbox.width() + bbox.xmin()) * width)
                right_eye_y = int((right_eye.y() * bbox.height() + bbox.ymin()) * height)
                Left_eye = (f"x: {left_eye_x:.2f} y: {left_eye_y:.2f}")
                Right_eye = (f"x: {right_eye_x:.2f} y: {right_eye_y:.2f}")       

                left_ear = points[3]  # left ear
                right_ear = points[4]  # right ear
                left_ear_x = int((left_ear.x() * bbox.width() + bbox.xmin()) * width)
                left_ear_y = int((left_ear.y() * bbox.height() + bbox.ymin()) * height)
                right_ear_x = int((right_ear.x() * bbox.width() + bbox.xmin()) * width)
                right_ear_y = int((right_ear.y() * bbox.height() + bbox.ymin()) * height)
                Left_ear = (f" x: {left_ear_x:.2f} y: {left_ear_y:.2f}") 
                Right_ear = (f"x: {right_ear_x:.2f} y: {right_ear_y:.2f}")

                left_shoulder = points[5]  # left shoulder
                right_shoulder = points[6]  # right shoulder
                left_shoulder_x = int((left_shoulder.x() * bbox.width() + bbox.xmin()) * width)
                left_shoulder_y = int((left_shoulder.y() * bbox.height() + bbox.ymin()) * height)
                right_shoulder_x = int((right_shoulder.x() * bbox.width() + bbox.xmin()) * width)
                right_shoulder_y = int((right_shoulder.y() * bbox.height() + bbox.ymin()) * height)
                Left_shoulder = (f"x: {left_shoulder_x:.2f} y: {left_shoulder_y:.2f}") 
                Right_shoulder = (f"x: {right_shoulder_x:.2f} y: {right_shoulder_y:.2f}")

                left_elbow = points[7]  # left elbow
                right_elbow = points[8]  # right elbow
                left_elbow_x = int((left_elbow.x() * bbox.width() + bbox.xmin()) * width)
                left_elbow_y = int((left_elbow.y() * bbox.height() + bbox.ymin()) * height)
                right_elbow_x = int((right_elbow.x() * bbox.width() + bbox.xmin()) * width)
                right_elbow_y = int((right_elbow.y() * bbox.height() + bbox.ymin()) * height)
                Left_elbow = (f"x: {left_elbow_x:.2f} y: {left_elbow_y:.2f}") 
                Right_elbow = (f"x: {right_elbow_x:.2f} y: {right_elbow_y:.2f}")

                left_wrist = points[9]  # left hand
                right_wrist = points[10]  # right hand
                left_wrist_x = int((left_wrist.x() * bbox.width() + bbox.xmin()) * width)
                left_wrist_y = int((left_wrist.y() * bbox.height() + bbox.ymin()) * height)
                right_wrist_x = int((right_wrist.x() * bbox.width() + bbox.xmin()) * width)
                right_wrist_y = int((right_wrist.y() * bbox.height() + bbox.ymin()) * height)
                Left_wrist = (f"x: {left_wrist_x:.2f} y: {left_wrist_y:.2f}")
                Right_wrist = (f"x: {right_wrist_x:.2f} y: {right_wrist_y:.2f}")


                left_hip = points[11]  # left groin
                right_hip = points[12]  # right groin
                left_hip_x = int((left_hip.x() * bbox.width() + bbox.xmin()) * width)
                left_hip_y = int((left_hip.y() * bbox.height() + bbox.ymin()) * height)
                right_hip_x = int((right_hip.x() * bbox.width() + bbox.xmin()) * width)
                right_hip_y = int((right_hip.y() * bbox.height() + bbox.ymin()) * height)
                Left_hip = (f"x: {left_hip_x:.2f} y: {left_hip_y:.2f}") 
                Right_hip = (f"x: {right_hip_x:.2f} y: {right_hip_y:.2f}")


                left_knee = points[13]  # left knee
                right_knee = points[14]  # right knee
                left_knee_x = int((left_knee.x() * bbox.width() + bbox.xmin()) * width)
                left_knee_y = int((left_knee.y() * bbox.height() + bbox.ymin()) * height)
                right_knee_x = int((right_knee.x() * bbox.width() + bbox.xmin()) * width)
                right_knee_y = int((right_knee.y() * bbox.height() + bbox.ymin()) * height)
                Left_knee = (f"x: {left_knee_x:.2f} y: {left_knee_y:.2f}")
                Right_knee = (f"x: {right_knee_x:.2f} y: {right_knee_y:.2f}")

                left_ankle = points[15]  # left foot
                right_ankle = points[16]  # right foot
                left_ankle_x = int((left_ankle.x() * bbox.width() + bbox.xmin()) * width)
                left_ankle_y = int((left_ankle.y() * bbox.height() + bbox.ymin()) * height)
                right_ankle_x = int((right_ankle.x() * bbox.width() + bbox.xmin()) * width)
                right_ankle_y = int((right_ankle.y() * bbox.height() + bbox.ymin()) * height)
                Left_ankle = (f"x: {left_ankle_x:.2f} y: {left_ankle_y:.2f}")
                Right_ankle = (f"x: {right_ankle_x:.2f} y: {right_ankle_y:.2f}")


                # if user_data.use_frame:
                #     cv2.circle(frame, (nose_x, nose_y), 5, (0, 255, 0), -1) 

                #     cv2.circle(frame, (left_eye_x, left_eye_y), 5, (0, 255, 0), -1)  
                #     cv2.circle(frame, (right_eye_x, right_eye_y), 5, (0, 255, 0), -1) 

                #     cv2.circle(frame, (left_ear_x, left_ear_y), 5, (0, 255, 0), -1)  
                #     cv2.circle(frame, (right_ear_x, right_ear_y), 5, (0, 255, 0), -1)  

                #     cv2.circle(frame, (left_shoulder_x, left_shoulder_y), 5, (0, 255, 0), -1)  
                #     cv2.circle(frame, (right_shoulder_x, right_shoulder_y), 5, (0, 255, 0), -1)  

                #     cv2.circle(frame, (left_elbow_x, left_elbow_y), 5, (0, 255, 0), -1)  
                #     cv2.circle(frame, (right_elbow_x, right_elbow_y), 5, (0, 255, 0), -1)  

                #     cv2.circle(frame, (left_wrist_x, left_wrist_y), 5, (0, 255, 0), -1)  
                #     cv2.circle(frame, (right_wrist_x, right_wrist_y), 5, (0, 255, 0), -1)

                #     cv2.circle(frame, (left_hip_x, left_hip_y), 5, (0, 255, 0), -1)  
                #     cv2.circle(frame, (right_hip_x, right_hip_y), 5, (0, 255, 0), -1) 

                #     cv2.circle(frame, (left_knee_x, left_knee_y), 5, (0, 255, 0), -1)  
                #     cv2.circle(frame, (right_knee_x, right_knee_y), 5, (0, 255, 0), -1) 

                #     cv2.circle(frame, (left_ankle_x, left_ankle_y), 5, (0, 255, 0), -1)  
                #     cv2.circle(frame, (right_ankle_x, right_ankle_y), 5, (0, 255, 0), -1)

                if ((left_wrist_y -right_wrist_y) < 20):

                    result = "open the gate"
                    video_with_text = {
                    "frame" : frame_count,
                    "detection" : persion,
                    "noise" : Nose,
                    "left_eye" : Left_eye,
                    "right_eye" : Right_eye,
                    "left_ear" : Left_ear,
                    "right_ear" : Right_ear,
                    "left_shoulder" : Left_shoulder,
                    "right_shoulder" : Right_shoulder,
                    "left_elbow" : Left_elbow,
                    "right_elbow" : Right_elbow,
                    "left_wrist" : Left_wrist,
                    "right_wrist" : Right_wrist,
                    "left_hip" : Left_hip,
                    "right_hip" : Right_hip,
                    "left_knee" : Left_knee,
                    "right_knee" : Right_knee,
                    "left_ankle" : Left_ankle,
                    "right_ankle" : Right_ankle,
                    "result" : result
                }
                    video_with_text = json.dumps(video_with_text, indent=20)
                    mqtt_client.publish(MQTT_TOPIC, video_with_text)

                elif ((right_wrist_y - nose_y) < 200):

                    result = "close the gate"
                    video_with_text = {
                    "frame" : frame_count,
                    "detection" : persion,
                    "noise" : Nose,
                    "left_eye" : Left_eye,
                    "right_eye" : Right_eye,
                    "left_ear" : Left_ear,
                    "right_ear" : Right_ear,
                    "left_shoulder" : Left_shoulder,
                    "right_shoulder" : Right_shoulder,
                    "left_elbow" : Left_elbow,
                    "right_elbow" : Right_elbow,
                    "left_wrist" : Left_wrist,
                    "right_wrist" : Right_wrist,
                    "left_hip" : Left_hip,
                    "right_hip" : Right_hip,
                    "left_knee" : Left_knee,
                    "right_knee" : Right_knee,
                    "left_ankle" : Left_ankle,
                    "right_ankle" : Right_ankle,
                    "result" : result
                }
                    video_with_text = json.dumps(video_with_text, indent=20)
                    mqtt_client.publish(MQTT_TOPIC, video_with_text)  # 发布到MQTT主题

                else:
                    video_with_text = {
                    "frame" : frame_count,
                    "detection" : persion,
                    "noise" : Nose,
                    "left_eye" : Left_eye,
                    "right_eye" : Right_eye,
                    "left_ear" : Left_ear,
                    "right_ear" : Right_ear,
                    "left_shoulder" : Left_shoulder,
                    "right_shoulder" : Right_shoulder,
                    "left_elbow" : Left_elbow,
                    "right_elbow" : Right_elbow,
                    "left_wrist" : Left_wrist,
                    "right_wrist" : Right_wrist,
                    "left_hip" : Left_hip,
                    "right_hip" : Right_hip,
                    "left_knee" : Left_knee,
                    "right_knee" : Right_knee,
                    "left_ankle" : Left_ankle,
                    "right_ankle" : Right_ankle,
                    "result" : "no result"
                }
                    video_with_text = json.dumps(video_with_text, indent=20)
                    mqtt_client.publish(MQTT_TOPIC, video_with_text)  # 发布到MQTT主题

            if user_data.use_frame:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # 转换为BGR格式
                user_data.set_frame(frame)

                # 降低分辨率
                scale_percent = 25  # 降低50%的分辨率，可以根据需要调整
                width = int(frame.shape[1] * scale_percent / 100)
                height = int(frame.shape[0] * scale_percent / 100)
                resized_frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

                # 将视频帧转换为 Base64 编码
                _, buffer = cv2.imencode('.jpg', resized_frame)
                frame_base64 = base64.b64encode(buffer).decode('utf-8')
                

                # 将 string_to_print 添加到 Base64 编码的视频流末尾
                video = f"{frame_base64}"

                video_with_text = {
                    "frame" : frame_count,
                    "detection" : persion,
                    "noise" : Nose,
                    "left_eye" : Left_eye,
                    "right_eye" : Right_eye,
                    "left_ear" : Left_ear,
                    "right_ear" : Right_ear,
                    "left_shoulder" : Left_shoulder,
                    "right_shoulder" : Right_shoulder,
                    "left_elbow" : Left_elbow,
                    "right_elbow" : Right_elbow,
                    "left_wrist" : Left_wrist,
                    "right_wrist" : Right_wrist,
                    "left_hip" : Left_hip,
                    "right_hip" : Right_hip,
                    "left_knee" : Left_knee,
                    "right_knee" : Right_knee,
                    "left_ankle" : Left_ankle,
                    "right_ankle" : Right_ankle,
                }

                video_with_text = json.dumps(video_with_text, indent=20)

                # 发送 Base64 编码的视频流到 MQTT 主题
                mqtt_client.publish(MQTT_TOPIC, video_with_text)

  

    # print(string_to_print)
    return Gst.PadProbeReturn.OK


class GStreamerPoseEstimationApp(GStreamerApp):
    def __init__(self, args, user_data):
        # Call the parent class constructor
        super().__init__(args, user_data)
        # Additional initialization code can be added here
        # Set Hailo parameters these parameters should be set based on the model used
        self.batch_size = 2
        self.network_width = 640
        self.network_height = 640
        self.network_format = "RGB"
        self.default_postprocess_so = os.path.join(self.postprocess_dir, 'libyolov8pose_post.so')
        self.post_function_name = "filter"
        self.hef_path = os.path.join(self.current_path, './hailomodel/yolov8s_pose_h8l_pi.hef')
        self.app_callback = app_callback
        
        # Set the process title
        setproctitle.setproctitle("Hailo Pose Estimation App")

        self.create_pipeline()

    def get_pipeline_string(self):

        if (self.source_type == "rpi"):
            source_element = f"libcamerasrc name=src_0 auto-focus-mode=2 ! "
            source_element += f"video/x-raw, format={self.network_format}, width=1536, height=864 ! "
            source_element += QUEUE("queue_src_scale")
            source_element += f"videoscale ! "
            source_element += f"video/x-raw, format={self.network_format}, width={self.network_width}, height={self.network_height}, framerate=30/1 ! "
        
        elif (self.source_type == "usb"):
            source_element = f"v4l2src device={self.video_source} name=src_0 ! "
            source_element += f"video/x-raw, width=640, height=480, framerate=30/1 ! "
        else:  
            source_element = f"filesrc location={self.video_source} name=src_0 ! "
            source_element += QUEUE("queue_dec264")
            source_element += f" qtdemux ! h264parse ! avdec_h264 max-threads=2 ! "
            source_element += f" video/x-raw,format=I420 ! "

        source_element += QUEUE("queue_scale")
        source_element += f"videoscale n-threads=2 ! "
        source_element += QUEUE("queue_src_convert")
        source_element += f"videoconvert n-threads=2 name=src_convert qos=false ! "
        source_element += f"video/x-raw, format={self.network_format}, width={self.network_width}, height={self.network_height}, pixel-aspect-ratio=1/1 ! "
        
        pipeline_string = "hailomuxer name=hmux "
        pipeline_string += source_element
        pipeline_string += "tee name=t ! "
        pipeline_string += QUEUE("bypass_queue", max_size_buffers=20) + "hmux.sink_0 "
        pipeline_string += "t. ! " + QUEUE("queue_hailonet")
        pipeline_string += "videoconvert n-threads=2 ! "
        pipeline_string += f"hailonet hef-path={self.hef_path} batch-size={self.batch_size} force-writable=true ! "
        pipeline_string += QUEUE("queue_hailofilter")
        pipeline_string += f"hailofilter function-name={self.post_function_name} so-path={self.default_postprocess_so} qos=false ! "
        pipeline_string += QUEUE("queue_hmuc") + " hmux.sink_1 "
        pipeline_string += "hmux. ! " + QUEUE("queue_hailo_python")
        pipeline_string += QUEUE("queue_user_callback")
        pipeline_string += f"identity name=identity_callback ! "
        pipeline_string += QUEUE("queue_hailooverlay")
        pipeline_string += f"hailooverlay ! "
        pipeline_string += QUEUE("queue_videoconvert")
        pipeline_string += f"videoconvert n-threads=2 qos=false ! "
        pipeline_string += QUEUE("queue_hailo_display")

        pipeline_string += f"videoconvert ! openh264enc ! rtph264pay ! udpsink host=192.168.49.160 port=2000" 

        # pipeline_string += f"fpsdisplaysink video-sink={self.video_sink} name=hailo_display sync={self.sync} text-overlay={self.options_menu.show_fps} signal-fps-measurements=true "
        # pipeline_string += f"videoconvert ! openh264enc ! rtph264pay ! udpsink host=192.168.49.160 port=2000" 

        print(pipeline_string)
        return pipeline_string

if __name__ == "__main__":

    user_data = user_app_callback_class()
    parser = get_default_parser()
    args = parser.parse_args()
    app = GStreamerPoseEstimationApp(args, user_data)
    app.run()