# encoding:utf8
__author__ = 'sijiu'
from init import initJsonData
from flask import Response, Flask, request,jsonify
import os
import json
from flask_cors import CORS

current_path = os.path.dirname(__file__)
root_dir = os.path.dirname(current_path)

app = Flask(__name__)

CORS(app, resources=r'/*')

# 解决jsonify中文显示为ascii码的问题
app.config["JSON_AS_ASCII"] = False


@app.route("/image", methods=['post', 'get'])
def getImage():
    path = request.args.get('path')
    print(path)
    path = current_path + "\\images\\" + path
    # path = os.path.abspath(path)
    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp


@app.route("/data",methods=['post','get'])
def getData():
    s = json.load(open(current_path+'\\mockData.json','r',encoding='utf-8'))
    print(s,type(s))
    return jsonify(s)

#  http://127.0.0.1:5000/like?type=classification&&model=alexnet
@app.route("/like",methods=['post','get'])
def like():
    model_type = request.args.get("type")
    model_name = request.args.get("model")
    s = json.load(open(current_path+'\\mockData.json','r',encoding='utf-8'))
    s["model_type"][model_type]["models"][model_name]["likes"] += 1
    with open(current_path+'\\mockData.json', 'w',encoding='utf-8') as write_f:
        write_f.write(json.dumps(s, indent=4, ensure_ascii=False))
    return jsonify(s["model_type"][model_type]["models"][model_name]["likes"])

@app.route("/dislike",methods=['post','get'])
def dislike():
    model_type = request.args.get("type")
    model_name = request.args.get("model")
    s = json.load(open(current_path+'\\mockData.json','r',encoding='utf-8'))
    if s["model_type"][model_type]["models"][model_name]["likes"] > 0:
        s["model_type"][model_type]["models"][model_name]["likes"] -= 1
        with open(current_path+'\\mockData.json', 'w',encoding='utf-8') as write_f:
            write_f.write(json.dumps(s, indent=4, ensure_ascii=False))
        return jsonify(s["model_type"][model_type]["models"][model_name]["likes"])
    else:
        return jsonify(s["model_type"][model_type]["models"][model_name]["likes"])

if __name__ == "__main__":
    # 初始化json数据（补充点赞，浏览，默认样例图片数据）
    initJsonData()
    app.run()


# app.run(host='0.0.0.0',port=4949, debug=True)