# author sqz
# date 2020/3/4 14:05
# file_name 模拟请求
import requests,time

for i in range(1000):
    res=requests.get("http://127.0.0.1:8000/api/v1/categorys/")
    print(time.time(),"当前次数",i)
    print(res.json())