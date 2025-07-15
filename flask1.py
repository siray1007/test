from flask import Flask,request

app = Flask(__name__)

#http://127.0.0.1:5000/index->执行index
##http://127.0.0.1:5000/index?age=20&pwd=123>执行index并接收20和123（传参）
@app.route("/index")
def index():
    age = request.args.get("age")
    pwd = request.args.get("pwd")
    print(age,pwd)
    return"成功"

#http://127.0.0.1:5000/home->执行home
@app.route("/home")
def home():
    age = request.args.get("age")
    pwd = request.args.get("pwd")
    print(age,pwd)

    return"失败"

if __name__ == '__main__':
    app.run()