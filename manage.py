#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role, Permission, Post
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

# This is handy if you want to include a bunch of defaults in your shell to save typing lots of import statements.
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission,
                Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# Run the test with python manager.py test
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.Testloader().discover('tests')
    unittest.TestTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
