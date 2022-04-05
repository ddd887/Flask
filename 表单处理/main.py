import flask
from flask import *
from datetime import timedelta

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templates' #模板文件
            )

@app.route('/chuli',methods=['POST'])
def chuli():
    if request.method=="POST":
        username = request.form.get("uname")
        password = request.form.get("passwd")
        print("用户名提交了"+username+"密码提交了"+password)
    return render_template('chuli.html')
    pass

@app.route('/test1')
def test1():
    return render_template('test1.html')
    pass

#装饰器,关联路由
@app.route('/')
def index():
    return "haha"
    pass

#404重定向
@app.errorhandler(404)
def page_not_found(e):
    return '你出错了',404
    pass

if __name__ == '__main__':
    app.run()
