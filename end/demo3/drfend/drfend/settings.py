"""
Django settings for drfend project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i89xxsik_9#y&j&u*(nj+jqbzyi&vlon(rrnq9e+=m(dtys(tk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'rest_framework',
    'rest_framework_jwt',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drfend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drfend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIAFIELS_DIRS = [os.path.join(BASE_DIR, 'media')]

# 此处可以对DJangoRestFrameWork重新配置
REST_FRAMEWORK = {
    # Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    # 默认的权限配置  每一个http方法都可以有对应的权限配置
    # 全局配置  优先级高于视图类中的配置
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    # 全局认证  优先级高于视图类中的配置
    'DEFAULT_AUTHENTICATION_CLASSES': [

        'rest_framework_simplejwt.authentication.JWTAuthentication',



        # 只能使用http协议  在服务器数据库中存放一张表  增加服务器开销
        # 'rest_framework.authentication.tokenAythenticaton'


        # 默认使用session认证
        # coolie与session
        # cookie是存储在浏览器上的非敏感数据
        # session为存储在服务器上的敏感数据  但是session离不开cookie   因为session的sessionid存储在浏览器中
        # 发起请求时  需要在cookie中携带sessionid  csrftoken   在header中携带X-CSRFToken  zhi可以在浏览器登录之后找cookie复制
        # 用户不能退出
        # 'rest_framework.authentication.SessionAuthentication',


        # 默认首先使用session认证    再使用 用户名密码认证
        # 发起请求时  可以将用户密码  进行编码  下入Authorization中然后发起请求
        # 将请求中携带的HTTP_AUTHORIZATION 进行编码 类似于Basic YWRtaW46MIIzNDU2 进行解码处理得到对应的用户 获取用户成功 认证成功  获取失败 认证失败
        # 每次都需要提供用户名密码
        # 'rest_framework.authentication.BasicAuthentication'
    ],
    #配置全局的频次限制类  实现反爬
    # 'DEFAULT_THROTTLE_CLASSES': ["rest_framework.throttling.AnonRateThrottle",
    #                              "rest_framework.throttling.UserRateThrottle"],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'user': '2/day',
    #     'anon': '1/day',
    # },
    #全局配置分页
    # 'DEFAULT_PAGINATION_CLASS': "rest_framework.pagination.LimitOffsetPagination",
    # 'DEFAULT_PAGINATION_CLASS': "rest_framework.pagination.PageNumberPagination",
    # 'PAGE_SIZE': 2,

    #全局过滤
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

AUTH_USER_MODEL = 'shop.User'

#自定义用户类  应用名.文件名.认证类名
AUTHENTICATION_BACKENDS=("shop.authbackend.MyLoginBackebd",)

# 允许跨域
CORS_ORIGIN_ALLOW_ALL = True
