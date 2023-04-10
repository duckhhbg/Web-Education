from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from PIL import Image
import cv2
import os
import datetime
import pickle
from .models import Auto_Camera

# vcap = cv2.VideoCapture("rtsp://admin:admin@192.168.1.78:554/30", cv2.CAP_FFMPEG)
vcap = cv2.VideoCapture(0)
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


# def Auto(request):
#     if request.method == 'POST':
#         getTime = request.POST['getTime']
#         Timer = request.POST['Timer']
#         Counter = request.POST['Counter']
#         print('Đã nhận được giá trị getTime: ', getTime)
#         print('Đã nhận được giá trị Timer: ', Timer)
#         print('Đã nhận được giá trị Counter: ', Counter)
#         if not getTime or not Timer or not Counter:
#             print("Thông báo: Cần nhập đầy đủ thông tin.")
#         else:
#             time_obj = datetime.datetime.strptime(getTime, '%H:%M')
#             # Tính toán khoảng thời gian giữa thời gian hiện tại và thời gian trong biến getTime
#             minutes = time_obj.hour * 60 + time_obj.minute
#             print('Lấy về: ', minutes)
#             # Lưu các giá trị vào file
#             with open('data.pkl', 'wb') as f:
#                 pickle.dump((getTime, Timer, Counter, minutes), f)
#             setUpTime()
#     return redirect('index')
#
#
# def setUpTime():
#     with open('data.pkl', 'rb') as f:
#         getTime, Timer, Counter, minutes = pickle.load(f)
#     GETTIME = int(minutes) + int(Timer)
#     # while True:
#     #     now = datetime.datetime.now()
#     #     minute = now.minute
#     #     hour = now.hour
#     #     read_time = hour * 60 + minute
#     #     print('Thực tế: ', read_time)
#     #     LimitTime = GETTIME - read_time
#     #     print('Khoảng thời gian còn lại: ', LimitTime)
#     #     if(LimitTime > 0):
#     #         return redirect('index')
#     #     if(LimitTime <= 0):
#     #         print("Đã hết thời gian rồi!!!!!!!!!!!!!!!")
#     #         return redirect('index')
#
#     # time_diff = now - datetime.fromtimestamp(GETTIME)
#     # print(f'Thời gian giữa thời điểm hiện tại và GETTIME là: {time_diff.total_seconds()} giây')

def Auto(request):
    global Timer, Counter
    if request.method == 'POST':
        Timer = request.POST['Timer']
        Counter = request.POST['Counter']
        print('Đã nhận được giá trị Timer: ', Timer)
        print('Đã nhận được giá trị Counter: ', Counter)
        if not Timer or not Counter:
            print("Thông báo: Cần nhập đầy đủ thông tin.")
        else:
            print("Nhận được đầy đủ thông tin rồi. Bắt đầu làm việc đây")
            auto = Auto_Camera(Timers=Timer, Couters=Counter)
            auto.save()
            print("Đã lưu thông tin rồi đây")
    return redirect('index')

def Camera_Auto(request):
    info = Auto_Camera.objects.values()
    print('Thông tin nhận được: ', info)
    queryset = Auto_Camera.objects.filter(id__in=[obj['id'] for obj in info])
    for obj in queryset:
        # truy xuất các trường trong đối tượng
        id = obj.id
        timers = obj.Timers
        counters = obj.Couters
        # sử dụng các giá trị đó để làm gì đó

        print(f"Với {id} thì TIMERS là: {timers} và COUNTER là: {counters}")



    return redirect('index')