# encoding:utf8
from init import initJsonData
from flask import Response, Flask, request,jsonify
import os,random,string
import json
from flask_cors import CORS

current_path = os.path.dirname(__file__)
root_dir = os.path.dirname(current_path)

app = Flask(__name__)

CORS(app, resources=r'/*')

# 解决jsonify中文显示为ascii码的问题
app.config["JSON_AS_ASCII"] = False
class ImageStore():
    dir = ''

cur_image = ImageStore()


@app.route("/image", methods=['post', 'get'])
def getImage():
    path = request.args.get('path')
    # print(path)
    path = current_path + "\\images\\" + path
    # path = os.path.abspath(path)
    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp

@app.route("/sourceimage", methods=['post', 'get'])
def getSourceImage():
    path = request.args.get('name')
    # print(path)
    path = current_path + "\\source_images\\" + path
    # path = os.path.abspath(path)
    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp


@app.route("/data",methods=['post','get'])
def getData():
    s = json.load(open(current_path+'\\mockData.json','r',encoding='utf-8'))
    # print(s,type(s))
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


#  http://127.0.0.1:5000/views?type=classification&&model=alexnet
@app.route("/pageviews",methods=['post','get'])
def pageviews():
    model_type = request.args.get("type")
    model_name = request.args.get("model")
    s = json.load(open(current_path+'\\mockData.json','r',encoding='utf-8'))
    s["model_type"][model_type]["models"][model_name]["pageviews"] += 1
    with open(current_path+'\\mockData.json', 'w',encoding='utf-8') as write_f:
        write_f.write(json.dumps(s, indent=4, ensure_ascii=False))
    return jsonify(s["model_type"][model_type]["models"][model_name]["pageviews"])


@app.route('/upload',methods=['GET','POST'])
def uploadimage():
    #生成随机字符串，防止图片名字重复
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    #获取图片文件 name = upload
    img = request.files.get('image')
    #定义一个图片存放的位置 存放在static下面
    path = current_path+"\\source_images\\"
    #图片名称 给图片重命名 为了图片名称的唯一性
    imgName = ran_str+img.filename
    #图片path和名称组成图片的保存路径
    file_path = path+imgName
    cur_image.dir = file_path
    print(cur_image.dir)

    #保存图片
    img.save(file_path)
    #这个是图片的访问路径，需返回前端（可有可无）
    # url = '/sourceimage/'+imgName
    url = imgName
    #返回图片路径 到前端
    return url 

@app.route('/submit',methods=['GET','POST'])
def submit():
    j = request.json
    # image_name = request.args.get("image_url")
    # conda_env = request.args.get("conda_env")
    # args = request.args.get("args")
    # print("tututuut:::")
    print(j)
    return jsonify(j)



if __name__ == "__main__":
    # 初始化json数据（补充点赞，浏览，默认样例图片数据）
    initJsonData()
    app.run()


# app.run(host='0.0.0.0',port=4949, debug=True)