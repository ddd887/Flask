import flask
from flask import *

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templages' #模板文件
            )

#404重定向
@app.errorhandler(404)
def page_not_found(e):
    return '你出错了',404
    pass

@app.route('/a/<id>')
def a_page(id):
    #python参数进来都是string类型
    m_int = id
    m_str = "haha nihao"
    m_list = ["xiaoming","xiaohong","xiaoli"]
    return flask.render_template("tempa.html",mint=m_int,mstr=m_str,mlist=m_list)
#装饰器,关联路由
@app.route('/')
def index():
    return "haha"
    pass

if __name__ == '__main__':
    app.run()
