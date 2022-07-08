import os
import json
current_path = os.path.dirname(__file__)

default_data={
    "likes":0,
    "pageviews":0,
    "input_image_name":"default.webp",
    "output_image_name": "default.webp",
    "author":"DemoHub"
}

def initJsonData():
    # 初始化json数据（补充点赞，浏览量，默认样例图片数据）
    s = json.load(open(current_path+'\\mockData.json','r',encoding='utf-8'))
    for (type,type_data) in s["model_type"].items():
        for (model_name,model_data) in type_data["models"].items():
            print(model_name,model_data)
            for key in default_data:
                if not (key in model_data):
                    model_data[key] = default_data[key]
    with open(current_path+'\\mockData.json', 'w',encoding='utf-8') as write_f:
        write_f.write(json.dumps(s, indent=4, ensure_ascii=False))
    return 0

if __name__=="__main__":
    initJsonData()