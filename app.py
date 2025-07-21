import sys
import os
import click
from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


# 初始化Flask应用
app = Flask(__name__)

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置

# 初始化数据库扩展
db = SQLAlchemy(app)


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份


# 路由视图
@app.route('/home')
def welcome():
    return 'Welcome to My Watchlist!'


@app.context_processor  # 模板上下文处理函数
def inject_user():
    user = User.query.first()
    return dict(user=user)


@app.errorhandler(404)  # 错误处理函数
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    user = User.query.first()  # 读取用户记录
    movies = Movie.query.all()  # 读取所有电影记录
    return render_template('index.html', user=user, movies=movies)


@app.route('/user/<name>')
def user_page(name):
    return f'User:{name}'


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
    name = 'SIRAY'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息


if __name__ == '__main__':
    app.run()

# @app.route('/user/test')
# def user_test():
#     movie = Movie.query.first()  # 获取 Movie 模型的第一个记录（返回模型类实例）
#     movie.title  # 对返回的模型类实例调用属性即可获取记录的各字段数据
#     movie.year
#     Movie.query.all()  # 获取 Movie 模型的所有记录，返回包含多个模型类实例的列表

#     Movie.query.count()  # 获取 Movie 模型所有记录的数量

#     Movie.query.get(1)  # 获取主键值为 1 的记录

#     Movie.query.filter_by(title='Mahjong').first()  # 获取 title 字段值为 Mahjong 的记录

#     Movie.query.filter(Movie.title == 'Mahjong').first()  # 等同于上面的查询，但使用不同的过滤方法
