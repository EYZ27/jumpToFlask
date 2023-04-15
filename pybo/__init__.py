from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config
from flaskext.markdown import Markdown

# SQLite 설정 수정하기
# pk, fk 등의 제약조건 이름을 수동으로 설정하기 위한 딕셔너리
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)             # SQLite 설정 수정하기
    else:
        migrate.init_app(app, db)
    from . import models    # 모델을 플라스크의 migrate 기능이 인식하려면 import 과정이 필요하다.

    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    # @app.route('/') # 어노테이션: 경로를 지정해주는 함수. URL과 플라스크 코드를 매핑해주는 함수.
    # def hello_pybo():
    #     return 'Hello, Pybo!'

    return app
