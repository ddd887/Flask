import flask
from flask import *

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templages' #模板文件
            )

#一种传参方式
@app.route('/ac/<user>/<passwd>')
def c_page(user,passwd):
    return "this is a page %s ----- %s hahaha"%(user,passwd)       
            



#get请求传参
@app.route('/abc',method=['GET'])
def a_page():
    user_name = request.args.get('uname')
    user_pass = request.args.get('upass')
    return "this is a page %s --- %s hahaha"%(user_name,user_pass)
    pass

#post请求传参
@app.route('/ab',method=['POST'])
def b_page():
    user_name = request.form.get('uname')
    user_pass = request.form.get('upass')
    return "this is a page %s --- %s hahaha"%(user_name,user_pass)
    pass

#装饰器,关联路由
@app.route('/')
def index():
    return "haha"
    pass

if __name__ == '__main__':
    app.run()
