from app import app#从app包中导入 app这个实例

#2个路由
@app.route('/')
@app.route('/index')
#1个视图函数
def index():
	return "Hello,World!"#返回一个字符串