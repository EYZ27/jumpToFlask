import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # 데이터베이스 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy의 이벤트를 처리하는 옵션. 파이보에 필요하지 않으므로 비활성화.
# URI 설정에 의해 SQLite 데이터베이스가 사용되고 데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장된다.
# 위 변수명은 다른 것으로 설정하지 못한다. 똑같이 써주자.
SECRET_KEY = "dev"