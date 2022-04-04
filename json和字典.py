import flask
from flask import *

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templages' #模板文件
            )

@app.route('/abc')
def a_page():
    #定义一个字典
    json_dict = {
        "name":"xiaoli"
        "age":"89"
        "score":"100"
    }
    #字典转化为json字符串
    result = json.dumps(json_dict)
    #json转化为字典
    dict1 = json.loads('{"age":"89","name":"xiaoli","score":"100"}')
    print(dict1["name"])

    return 'x'
    pass
#装饰器,关联路由
@app.route('/')
def index():
    return "haha"
    pass

if __name__ == '__main__':
    app.run()