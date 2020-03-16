# author sqz
# date 2020/3/16 19:07
# file_name factory

"""
flask :应用工厂
"""
# 1.引入Flask
from flask import Flask, request, render_template, flash, redirect


def create_app():
    """
    应用刚才负责应用所有相关内容  包括创建  配置
    :return:
    """
    # 2.构造Flask对象  其实就是一个WSGI应用   __name__为flask寻找static 以及temolates 提供支持
    app = Flask(__name__)

    @app.route("/")
    def index():
        bookList = [
            {
                "ID": 101,
                "Name": "神雕侠侣"
            },
            {
                "ID": 102,
                "Name": "射雕英雄传"
            },
            {
                "ID": 103,
                "Name": "雪山飞狐"
            }

        ]
        return render_template("index.html", bl=bookList)

    # 注册404  路由自定义错误  页面
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html")

    # 4.绑定路由与视图函数  methods表明当前路由所接受的http方法
    @app.route("/login", methods=["GET", "POST"])
    def login():
        # 5.在flask中请求对象封装在request中  request代表请求  引入request  from flask import request
        # print("登陆中的", request, request.method,dir(request))
        if request.method == "GET":
            # 7.使用render_template渲染jinja2模板
            # 模板文件夹和python模板同级
            # 8.静态资源static用法等同templates
            # render_template第二个参数为传入模板中的对象
            categoryList = [
                               {
                                   "ID": 101,
                                   "Name": "汽车"
                               },
                               {
                                   "ID": 102,
                                   "Name": "食品"
                               }
                           ],
            user = {
                "Name": "sqz"
            }
            return render_template("login.html", cl=categoryList, u=user)
        elif request.method == "POST":
            # 6.从form中提取表单参数
            username = request.form.get("username")
            password = request.form.get("password")

            error = None
            if not username:
                error = "用户名必须填写"
            elif not password:
                error = "密码必须填写"
            # 9.使用flash可以将参数传入下一个请求  此处error写入下一个请求
            if error:
                flash(error)  # 此处error写入下一个请求
                return redirect("/login")  # 重定向
            else:
                return '%s--%s' % (username, password)

    @app.route("/regist", methods=["GET", "POST"])
    def regist():
        if request.method == "GET":
            return render_template("regist.html")
        elif request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            password2 = request.form.get("password2")
            error = None
            if not username:
                error = "用户名不能为空"
            elif not password:
                error = "密码不能为空"
            elif not password2:
                error = "重复密码不能为空"
            if error:
                flash(error)  # 此处error写入下一个请求
                return redirect("/regist")  # 重定向
            else:
                return '注册成功: %s--%s' % (username, password)

    # 10.session是存储在服务器上的加密信息  会将sessionid保存在cookie
    app.secret_key = "Q\x8e\xa5[\xefu.\xb0\xd5\xfb\xd7\xd2@)e>\x06\x82\x92/\x8awO\xc2"
    return app
