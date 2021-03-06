#!/bin/bash
set -x #echo on
VIDSOURCE="rtsp://192.168.50.242:8554/"
CAMSOURCE="/dev/video0"
AUDIOSOURCE="hw:1,0"
AUDIO_OPTS="-f alsa -ac 1"
VIDEO_OPTS="-s 640x480 -framerate 10 -c:v libx264 -b:v 800000"
OUTPUT_HLS="-r 10 -hls_time 10 -hls_list_size 10 -start_number 1"
OUTPUT_NAME="av10FPS"
COMMAND="ffmpeg $AUDIO_OPTS -i $AUDIOSOURCE -i $CAMSOURCE -y $VIDEO_OPTS $OUTPUT_HLS $OUTPUT_NAME.m3u8"



$COMMAND


