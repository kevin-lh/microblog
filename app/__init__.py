from flask import Flask
#从flask包中导入Flask类
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app.config.from_object(Config)


login = LoginManager(app)
login.login_view='login'
#指定登录视图

db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象
#需要的话，可继续添加更多的变量
#print('等会谁（哪个包或模块）在使用我：',__name__)

from app import routes,model
#从app包中导入模块routes

#注：上面两个app是完全不同的东西。两者都是纯粹约定俗成的命名，可重命名其他内容。