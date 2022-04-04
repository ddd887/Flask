import flask
from flask import *

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templages' #模板文件
            )

@app.route('/abc',method=['GET','POST'])
def a_page():
    user_name = request.form.get('uname')
    user_pass = request.form.get('upass')
    return "this is a page %s hahaha"%(request.headers.get('User-agent'))  #也能改为request.path/.fullpath/.url/.baseurl/.user_agent.platform
    pass

#装饰器,关联路由
@app.route('/')
def index():
    return "haha"
    pass

if __name__ == '__main__':
    app.run()
