import requests
import base64
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

"""
API: https://console.faceplusplus.com.cn/documents/124332617
"""

beautify_url = "https://api-cn.faceplusplus.com/facepp/v1/3dface"
# 你创建的应用的 API Key 和 API Secret(也叫 Secret Key)
AK = 'D3lzCWVPavwiYGqFIP-2nFCcFtTVcKaw'
SK = 'rZrYCDPPoHi-Eohz8xU0UWZ0aCOZHf5A'

# 二进制方式打开图片
img_name = 'b.jpg'
f = open(img_name, 'rb')
# 转 base64
img_base64 = base64.b64encode(f.read())

# 使用 whitening、smoothing、thinface 三个可选参数，其他用默认值
data = {
    'api_key': AK,
    'api_secret': SK,
    'image_base64_1': img_base64
    }

r = requests.post(url=beautify_url, data=data)
html = json.loads(r.text)
# 解析base64图片
base64_data = html['obj_file']
with open('3D人脸重建.jpg', 'wb') as f:
    f.write(base64.b64decode(base64_data))


# file = open('3D人脸重建.jpg', 'wb')
# file.write(imgData)
# file.close()

