import requests
import base64
import os
import random
def convert(source, target):
    with open(source, "rb") as f:
        content = f.read()
    b64_img = base64.b64encode(content)

    headers = {
        'authority': 'ai.baidu.com',
        'sec-fetch-dest': 'empty',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',
        'dnt': '1',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://ai.baidu.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://ai.baidu.com/tech/imageprocess/style_trans',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': f'BAIDUID={random.random() * 10000000}:FG=1; BIDUPSID=A0BA4DB0795DBF7605429D834EB25C4A; PSTM=1581990270; MCITY=-289%3A; BDUSS=29rTnk5RUpORTJ2TmxJYjlvQ2FuNndaSE8tSnZFVXVJQXAxdlM0MWRHbmpDSnhlSUFBQUFBJCQAAAAAAAAAAAEAAADGERL1weO6xdPuur3UsQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAON7dF7je3ReT; delPer=0; cflag=13%3A3; BCLID=12612561071506155803; BDSFRCVID=QEtOJeC62xOTHAjuf5DC2MjtQMS_AG3TH6aoK5diRndnOaqom8y7EG0Pjf8g0KubzcDrogKK0eOTHk8F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbAeoKDaf-3bfTrmMtQ_M-4HbUb3a46KHD7yWCvpbhQcOR5Jj6K-X-PVDxnt-pRIamQnKRk-tqkK8MjO3MA--t4jyUvx3bcdKmDJMhn5aU7Isq0x0-nte-bQyp_Lb5jr3DOMahkM5l7xO-QVQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjTXjH-ttTLDJn3fL-082R6oDn8k-PnVep_k5-nZKxtqtjb9-pnp2t5tMqbJDxc85h_I0nnC05JnWncKWhka5nTCDRbkXPQahPrb2HJ405OT2DFO0KJcbRo0Hpb4hPJvyT88XnO7a5vlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVJO-KKCahDLCjx5; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=7; H_PS_PSSID=1430_31170_21110_31187_30906_30824_31085_26350_31195; Hm_lvt_8b973192450250dd85b9011320b455ba=1584692190,1584692292,1585712218,1585712509; Hm_lpvt_8b973192450250dd85b9011320b455ba=1585712526',
    }

    data = {
    'image': f'data:image/jpeg;base64,{b64_img.decode()}',
    'image_url': '',
    'type': 'https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans',
    'option': 'pencil'
    }

    response = requests.post('https://ai.baidu.com/aidemo', headers=headers, data=data)
    try:
        b64_res_img = response.json()["data"]["image"]
    except Exception as e:
        print(source , response.json()["msg"])
        return 

    with open(target, "wb") as f:
        f.write(base64.b64decode(b64_res_img))

def convert_all_img():
    target_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "img")
    new_target_dir =  os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "img2")
    for _file in os.listdir(target_dir):
        if _file.endswith("jpg") or _file.endswith("png"):
            print(os.path.join(target_dir, _file), os.path.join(new_target_dir, _file))
            convert(source=os.path.join(target_dir, _file), target=os.path.join(new_target_dir, _file))
        
    

if __name__ == "__main__":
    convert_all_img()