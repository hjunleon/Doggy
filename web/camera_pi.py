#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  camera_pi.py
#  
#  
#  
import time
import io
import threading
import cv2
#import picamera

capture = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
"""
if not capture.isOpened():
    print("Cannot open camera")
    exit()
"""


class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        #with picamera.PiCamera() as camera:
        # camera setup
        #camera.resolution = (320, 240)
        #camera.hflip = True
        #camera.vflip = True

        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

        # let camera warm up
        #camera.start_preview()
        #time.sleep(2)

        while True:
            ret, frame = capture.read()
            cls.frame = frame


        """

        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'jpeg',
                use_video_port=True):
            # store frame
            stream.seek(0)
            cls.frame = stream.read()

            # reset stream for next frame
            stream.seek(0)
            stream.truncate()

            # if there hasn't been any clients asking for frames in
            # the last 10 seconds stop the thread
            if time.time() - cls.last_access > 10:
                break
        
        """
        cls.thread = None
