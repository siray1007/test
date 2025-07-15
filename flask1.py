from flask import Flask

app = Flask(__name__)

#当http://127.0.0.1:5000/index时执行index
@app.route("/index")
def index():
    return"成功"



#当http://127.0.0.1:5000/home时执行home
@app.route("/home")
def home():
    return"失败"



if __name__ == '__main__':
    app.run(host="127.0.0.1",post=5000)