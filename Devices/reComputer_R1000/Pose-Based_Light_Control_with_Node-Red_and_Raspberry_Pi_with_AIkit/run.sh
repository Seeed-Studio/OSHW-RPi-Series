# !/bin/bash

folder="./hailomodel"
#filename=$(basename "$1")

# Check if the folder exists
if [ ! -d "$folder" ]; then
    # If the folder does not exist, create it
    mkdir -p "$folder"

    # Download the file into the created folder
    wget https://hailo-csdata.s3.eu-west-2.amazonaws.com/resources/hefs/h8l_rpi/yolox_s_leaky_h8l_mz.hef -P $folder
    wget https://hailo-csdata.s3.eu-west-2.amazonaws.com/resources/hefs/h8l_rpi/yolov6n.hef -P $folder
    wget https://hailo-csdata.s3.eu-west-2.amazonaws.com/resources/hefs/h8l_rpi/yolov8s_h8l.hef -P $folder
    wget https://hailo-csdata.s3.eu-west-2.amazonaws.com/resources/hefs/h8l_rpi/yolov8s_pose_h8l_pi.hef -P $folder
    wget https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.11.0/hailo8l/centernet_resnet_v1_18_postprocess.hef -P $folder
    wget https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.11.0/hailo8l/centernet_resnet_v1_50_postprocess.hef -P $folder
    wget https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.11.0/hailo8l/damoyolo_tinynasL20_T.hef -P $folder
    wget https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.11.0/hailo8l/nanodet_repvgg.hef -P $folder
    

    echo "Folder created and file downloaded successfully."
else
    # If the folder already exists, do nothing
    echo "Folder already exists. No action taken."
fi

source setup_env.sh
pip install setproctitle
pip install opencv-python
pip install paho-mqtt


python3 pose-estimation.py -i /dev/video0 -f
