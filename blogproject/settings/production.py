'''
存放线上环境配置
'''

from .common import *


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['hellodjango-blog-tutorial.xiaogejie.com']