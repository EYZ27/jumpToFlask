from flask import Blueprint, render_template

from pybo.models import Question


bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)
    # render_template 가 html 파일 내의 파이썬 코드를 다 rendering 시켜서 html 코드로 넣어준다.


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id) # 404 오류면 오류페이지를 내보내겠다
    return render_template('question/question_detail.html', question=question)
