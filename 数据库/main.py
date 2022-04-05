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
def chuli(pymysql=None):
    if request.method=="POST":
        username = request.form.get("uname")
        password = request.form.get("passwd")
        print("用户名提交了"+username+"密码提交了"+password)
    pass

    #打开数据库
    db = pymysql.connect(hosst="localhost",user="root",password="root",db="haha")
    #创建游标对象
    cursor = db.cursor()
    #sql语句
    sql = "select * from table1"
    #执行sql
    cursor.execute(sql)
    #确认
    db.commit()
    list1 = []
    for temp in cursor.fetchall():
        dict = {'名字':temp[1],'密码':temp[2]}
        list1.append(dict)
    print(list1)
    db.close()
    result = json.dumps(list1,sort_keys=True,ensure_ascii=False)
    return result
    #return render_template('chuli.html')
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
