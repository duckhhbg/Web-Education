import os
import json
import requests

# Thực hiện thiết lập quyền cho phép truy cập vào Google Drive
headers = {
    "Authorization": "Bearer ya29.a0Ael9sCNIpWxQYoPYdKoJs3MNKnjMs3tvURGScT23zaHXxK4MvJxNlaeEg8QLWl588n22lbaWUZeJTTvBzpd014qNms87CTGCHjqmsiQkKIv7omnd92K86XQB5oyQP70e6sAIdUjwZoWrCnnTnSzeee-Q4MD-aCgYKARMSARESFQF4udJhMatRBg0q5kXKhDyCXJkSxQ0163"
}

# Thực hiện thiết lập địa chỉ thư mục gửi lên trên Google Drive
folder_metadata = {
    "name": "Ảnh Backgroud",
    "parents": ["1uwPFRQyuO15MM_-arhYNErawhcWZlukY"],
    "mimeType": "application/vnd.google-apps.folder"
}

# Tạo thư mục trong Google Drive
r = requests.post("https://www.googleapis.com/drive/v3/files",
                  headers=headers,
                  json=folder_metadata)

folder_id = r.json()["id"]

# Lấy danh sách các tệp trong thư mục
path_Folder = "TEST"
files = os.listdir(path_Folder)

# Lặp qua danh sách các tệp và thực hiện tải từng tệp lên Google Drive
for file_name in files:
    file_metadata = {
        "name": file_name,
        "parents": [folder_id]
    }

    files = {
        "data": ("metadata", json.dumps(file_metadata), "application/json;charset=UTF-8"),
        "file": open(path_Folder + "/" + file_name, "rb")
    }

    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )

print('Đã thực hiện tải xong')