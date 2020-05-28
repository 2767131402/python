import requests
import base64
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

"""
API: https://console.faceplusplus.com.cn/documents/134252584
"""

beautify_url = "https://api-cn.faceplusplus.com/facepp/v2/beautify"
# 你创建的应用的 API Key 和 API Secret(也叫 Secret Key)
AK = 'Z6ijXb5_tKDKWOiE8xJHaiJn31epUYkM'
SK = 'y3__zFU8oO4lxZ59YOzDQz3MAe5n6gni'

# 可选参数，不填写，默认50
# 美白程度 0 - 100
whitening = 80
# 磨皮程度 0 - 100
smoothing = 80
# 瘦脸程度 0 - 100
thinface = 20
# 小脸程度 0 - 100
shrink_face = 50
# 大眼程度 0 - 100
enlarge_eye = 50
# 去眉毛程度 0 - 100
remove_eyebrow = 50
# 滤镜名称，不填写，默认无滤镜
filter_type = 'black_white'

# 二进制方式打开图片
img_name = 'a.png'
f = open(img_name, 'rb')
# 转 base64
img_base64 = base64.b64encode(f.read())

# 使用 whitening、smoothing、thinface 三个可选参数，其他用默认值
data = {
    'api_key': AK,
    'api_secret': SK,
    'image_base64': img_base64,
    'whitening': whitening,
    'smoothing': smoothing,
    'thinface': thinface,
    'shrink_face':shrink_face,
    'enlarge_eye':enlarge_eye,
    'remove_eyebrow':remove_eyebrow,
    'filter_type':filter_type
    }

r = requests.post(url=beautify_url, data=data)
html = json.loads(r.text)

# 解析base64图片
base64_data = html['result']
imgData = base64.b64decode(base64_data)
nparr = np.frombuffer(imgData, np.uint8)
img_res = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
img_res_BGR = cv2.cvtColor(img_res, cv2.COLOR_RGB2BGR)

# 将处理后的图片保存 方式一
matplotlib.image.imsave('图片美颜.png', img_res_BGR)

# 将处理后的图片保存 方式二
# with open('图片美颜.png', 'wb') as f:
#     f.write(imgData)

# 原始图片
img = cv2.imread(img_name)
img_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# 显示图片
fig, axs = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False, figsize=(50,50))
axs[0].imshow(img_BGR)
axs[1].imshow(img_res_BGR)
# 保存图片
# plt.savefig('testblueline.png')

# 不显示左坐标
plt.axis('off')
plt.show()