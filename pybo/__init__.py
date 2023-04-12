from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models    # 모델을 플라스크의 migrate 기능이 인식하려면 import 과정이 필요하다.

    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # @app.route('/') # 어노테이션: 경로를 지정해주는 함수. URL과 플라스크 코드를 매핑해주는 함수.
    # def hello_pybo():
    #     return 'Hello, Pybo!'

    return app
