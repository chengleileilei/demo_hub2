import os
import json
current_path = os.path.dirname(__file__)

default_data = {
    "introduction": {
        "tittle": {
            "en": "INTRODUCTION",
            "cn": "介绍"
        },
        "text": {
            "en": [
                "There is no model introduction information!",
                "For more information, please visit "
            ],
            "cn": [
                "暂无模型介绍信息！",
                "欲了解更多信息，请访问"
            ]
        },
        "link": {
            "text": {
                "en": "https://mmcheng.net",
                "cn": "https://mmcheng.net"
            },
            "url": "https://mmcheng.net"
        }
    },
    "likes": 0,
    "pageviews": 0,
    "input_image_name": "default.png",
    "output_image_name": "default.png",
    "author": "DemoHub"
}


def initJsonData():
    # 初始化json数据（补充点赞，浏览量，默认样例图片数据）
    s = json.load(open(current_path+'\\mockData.json', 'r', encoding='utf-8'))
    for (type, type_data) in s["model_type"].items():
        for (model_name, model_data) in type_data["models"].items():
            # print(model_name,model_data)
            for key in default_data:
                if not (key in model_data):
                    model_data[key] = default_data[key]
            # 设置默认conda环境为类名+模型名
            if "conda_env" not in model_data:
                model_data["conda_env"] = type + "_" + model_name
            # 设置默认name
            if "name" not in model_data:
                model_data["name"] = {
                    "en": model_name,
                    "cn": model_name
                }
            # 存在参数则设置参数默认值
            if "args" in model_data:
                for arg_name, arg_data in model_data["args"].items():
                    if (("default" not in arg_data) or (arg_data["default"] == "")):
                        arg_data["default"] =arg_data["values"][0]


    with open(current_path+'\\mockData.json', 'w', encoding='utf-8') as write_f:
        write_f.write(json.dumps(s, indent=4, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    initJsonData()
