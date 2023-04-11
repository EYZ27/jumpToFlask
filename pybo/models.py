from pybo import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # 플라스크는 데이터타입이 db.Integer이고 기본키로 설정한 속서은 값이 자동으로 증가하는 특징을 가지고 있다.
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))   # 답변을 질문에 참조할 때 / ForeignKey는 참조하는 값과 동일한 타입으로 만들어줘야 한다.
    question = db.relationship('Question', backref=db.backref('answer_set'))    # Question 테이블과 관계를 가진다. backref = 참조 명칭. 어떤 질문에 해당하는 객체가 a_question일 때, a_question.answer_set과 같은 코드로 해당 질문에 달린 답변들을 참조할 수 있다.
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    # 실제 파이썬 코드에서 질문을 삭제할 때 답변까지 모두 삭제하려면 코드가 추가로 필요하다.
    # question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))


