from flask import Flask, render_template, Response

# Raspberry Pi camera module (requires picamera package, developed by Miguel Grinberg)
#from camera_pi import Camera

import cv2, os, time

cap = None


#if os.environ.get('WERKZEUG_RUN_MAIN') or Flask.debug is False:
    #print("Inthread")
#cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    #print(cap)
cap = cv2.VideoCapture('rtsp://127.0.0.1:8554')
time.sleep(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#if not cap.isOpened():
#    print("cant open cam")
#    cap.release()
#    exit()
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)


app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera=None):
    """Video streaming generator function."""
    while True:
        ret, frame = cap.read()#camera.get_frame()
        if not ret:
            print("CANT CAPTURE")
            raise Exception 
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port =3000, debug=True, threaded=True)
        
    #cap.release()
