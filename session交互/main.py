import flask
from flask import *
from datetime import timedelta

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templates' #模板文件
            )
#配置加密字符串
app.config['SECRET_KEY']="key123"
#设置7天有效
app.config["PERMANENT_SESSION_LIFETIME"]="timedelta(days=7)"

@app.route('/login')
def b_page():
    response = flask.make_response('success')
    #设置session
    session['user_id']="20"
    session['vip'] = '0'
    return 'success'
    pass

@app.route('/a')
def a_page():
    #读取session
    user_id = session['user_id']
    vip = session['vip']
    return flask.render_template("tempa.html",user_id=user_id,vip=vip)
    pass


@app.route('/logout')
def logout():
    session.pop('user_id',None)
    session.pop('vip',None)
            
    #session['user_id'] = False

    #session.clear()
    return 'logout'
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
