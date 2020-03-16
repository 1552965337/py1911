# author sqz
# date 2020/3/16 14:40
# file_name generate_secret_key
import os

# 生成密钥
secret_key = os.urandom(24)
print(secret_key)