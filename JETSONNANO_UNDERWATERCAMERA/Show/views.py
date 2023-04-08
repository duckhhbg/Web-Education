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
    if request.method == 'POST':
        GT_1 = request.POST['Value_1']
        GT_2 = request.POST['Value_2']
        GT_3 = request.POST['Value_3']
        print('Đã nhận được giá trị 1: ', GT_1)
        print('Đã nhận được giá trị 2: ', GT_2)
        print('Đã nhận được giá trị 3: ', GT_3)
    ret, frame = vcap.read()
    localtime = time.localtime(time.time())
    read_time = str(localtime.tm_mday) + '-' + str(localtime.tm_mon) + '-' + str(
                localtime.tm_year) + '--' + str(localtime.tm_hour) + 'h' + str(localtime.tm_min) + 'm' + str(localtime.tm_sec) + 's' + "__" + str(GT_1) + "__" + str(GT_2) + "__" + str(GT_3) + "__"
    file_name = 'static/CAMERA/image_' + read_time + '.jpg'
    if file_name is not None:
        cv2.imwrite(file_name, frame)
    else:
        print("Có lỗi, không tìm thấy ảnh đầu vào!")
    Count()
    return redirect('index')


def getValue(req):
    if req.method == 'POST':
        GT_1 = req.POST['Value_1']
        GT_2 = req.POST['Value_2']
        GT_3 = req.POST['Value_3']
        print('Đã nhận được giá trị 1: ', GT_1)
        print('Đã nhận được giá trị 2: ', GT_2)
        print('Đã nhận được giá trị 3: ', GT_3)
    return render(req, 'index.html')