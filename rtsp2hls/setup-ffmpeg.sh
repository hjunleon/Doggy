#!/bin/bash
VIDSOURCE="rtsp://192.168.50.242:8554/"
CAMSOURCE="/dev/video0"
AUDIO_OPTS="-c:a aac -b:a 160000 -ac 2"
VIDEO_OPTS="-s 640x480 -framerate 10 -c:v libx264 -b:v 800000"
OUTPUT_HLS="-r 10 -hls_time 10 -hls_list_size 10 -start_number 1"
OUTPUT_NAME="testing10FPS"
ffmpeg -i "$CAMSOURCE" -y $AUDIO_OPTS $VIDEO_OPTS $OUTPUT_HLS $OUTPUT_NAME.m3u8


