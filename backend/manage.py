# import Flask Script object

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from run import app
from extensions import db

from apps.user.models import User
from apps.catalog.models import Catalog

# init manager object via app object
manager = Manager(app)

# init migrate object via app and db object
migrate = Migrate(app, db)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)


# 更新数据迁移
@manager.command
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    from flask_migrate import migrate, upgrade
    migrate()
    upgrade()


# 删除数据库里所有的表
@manager.command
def dropall():
    db.drop_all()
    print("all tables dropped! remember to delete directory: migrations")


# 创建admin用户，赋予superuser角色
@manager.command
def initrole():
    db.session.add(User(username="temp-admin", password="temp-pwd", roles='superuser'))
    db.session.commit()
    print("Roles added!")


# 初始化数据库
@manager.command
def initdb():
    db.session.add(Catalog(name='默认'))
    db.session.commit()
    print("Catalog added!")


if __name__ == '__main__':
    manager.run()
