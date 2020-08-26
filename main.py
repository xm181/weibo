#!/usr/bin/env python

from flask import Flask
from flask import redirect
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from libs.orm import db
from user.views import user_bp
from weibo.views import weibo_bp
from user.models import User
from weibo.models import Weibo

#初始化app
app = Flask(__name__)
app.secret_key = r'suq34898oiiuio*(*&998(*%4%^6Tkd,mf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xm124578!!@localhost:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 每次请求结束后都会自动提交数据库中的变动

#初始化manager
manager = Manager(app)

#初始化db和migrate
db.init_app(app)
migrate = Manager(app, db)
manager.add_command('db', MigrateCommand)

#注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(weibo_bp)

@app.route('/')
def home():
    '''首页'''
    return redirect('/weibo/index')

@manager.command
def create_test_weibo():
    '''创建微博测试数据'''
    users=User.fake_users(50)
    uid_list=[u.id for u in users]
    weibo.fake_weibos(uid_list,100)

if __name__ == "__main__":
    manager.run()
