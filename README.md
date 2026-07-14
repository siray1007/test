# Watchlist

一个基于 Flask 的电影清单 Web 应用，支持用户认证和电影记录的增删改查。

## 功能

- 🔐 用户注册与登录
- 🎬 电影清单管理（添加、编辑、删除）
- 🐳 Docker 支持
- 🧪 单元测试

## 技术栈

- **Python 3.10+**
- **Flask** - Web 框架
- **Flask-SQLAlchemy** - ORM
- **Flask-Login** - 用户认证
- **SQLite** - 数据库
- **Docker** - 容器化部署

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 初始化数据库
flask initdb

# 生成示例数据
flask forge

# 创建管理员
flask admin --username admin --password admin

# 启动服务
flask run
```

访问 http://localhost:5000 查看应用。

## Docker 部署

```bash
docker-compose up -d
```
