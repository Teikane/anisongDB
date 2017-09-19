import os
basedir = os.path.abspath(os.path.dirname(__file__))

#enable basic webform XXS prevention
WTF_CSRF_ENABLED = True
SECRET_KEY = 'insert-difficult-to-guess-phrase-here-jinrui-ni-eiko-aru'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'anisong.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')