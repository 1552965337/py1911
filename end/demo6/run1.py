# author sqz
# date 2020/3/16 9:44
# file_name run1

from factory import create_app

# 3.启动应用程序
if __name__ == "__main__":
    # 开发环境使用  debug=True自带重启服务器
    create_app().run()
