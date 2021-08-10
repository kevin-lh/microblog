from app import app, db
from app.model import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
#从app包中导入变量app（它是作为app包成员的变量）

if __name__ == '__main__':
    app.run(debug=True)