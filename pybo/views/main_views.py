from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')    # 주소 뒤에 /가 붙고 그 뒤에 주소...?


@bp.route('/hello')  # 두 칸 띄워 줘야 함
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))  # question의 _list를 찾아서 url을 반환해주는 함수 url_for
    # blueprint명 'question', 그 안에 함수명 '_list'

# 마지막 줄에 빈 칸 있어야 함
