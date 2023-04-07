from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from PIL import Image
import cv2
import time
import os

vcap = cv2.VideoCapture("rtsp://admin:admin@192.168.1.78:554/30", cv2.CAP_FFMPEG)
vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def Count():
    folder_path = "static/CAMERA/"
    count = 0
    files = os.listdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        try:
            with Image.open(file_path) as img:
                count += 1
        except:
            pass
    print("Số lượng ảnh trong file là: ", count)

def generate_frames():
    while True:
        ret, frame = vcap.read()
        if not ret:
            break
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@gzip.gzip_page
def livefe(request):
    try:
        return StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is to handle when the client disconnects
        pass

def index(request):
    return render(request, 'index.html')

def capture(request):
    ret, frame = vcap.read()
    localtime = time.localtime(time.time())
    read_time = str(localtime.tm_mday) + '-' + str(localtime.tm_mon) + '-' + str(
                localtime.tm_year) + '--' + str(localtime.tm_hour) + 'h' + str(localtime.tm_min) + 'm' + str(localtime.tm_sec) + 's'
    file_name = 'static/CAMERA/image_' + read_time + '.jpg'
    cv2.imwrite(file_name, frame)
    Count()
    return redirect('index')