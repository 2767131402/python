import requests

url = "https://fanyi.baidu.com/basetrans"

str = "哈哈哈"

query_string = {
    "query": str,"from": "zh",
    "to": "en","token": "5d3e8206ed19fa88fdd4bf5bd1608aa2",
    "sign": "47194.285547"
}

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "referer": "https://fanyi.baidu.com/?aldtype=16047",
    "cookie": "BAIDUID=2839E07806F18C579712A6C155C856E3:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1590550235; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1590550256; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1590550256; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1590550256; yjs_js_security_passport=b28418b88778deb4a545c8e91bc0dc202a496bf5_1590550265_js; BIDUPSID=2839E07806F18C579712A6C155C856E3; PSTM=1590557783; H_PS_PSSID=31730_1461_21098_31110_31253_31596_31606_31271_31463_31715_30823_26350; delPer=0; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598"
}
response = requests.post(url,data=query_string,headers=headers)
print(response.content.decode("gbk"))

