from pybo import db

question_hitter = db.Table(
    'question_hitter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)


question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)


answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)



# question table
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # 플라스크는 데이터타입이 db.Integer이고 기본키로 설정한 속성은 값이 자동으로 증가하는 특징을 가지고 있다.
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)  # 그러나 이미 있던 데이터에는 user_id 값이 없다. nullable을 False로 해두면 오류가 난다. server_default는 null 대신 임의의 값을 넣어준다. server_default를 사용하면 flask db upgrade 명령을 수행할 때 null이던 데이터에도 기본값이 저장된다. default를 새로 생성되는 데이터에만 기본값을 생성해준다.
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))
    hits = db.Column(db.Integer, nullable=True, server_default='0')


# answer table
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))   # 답변을 질문에 참조할 때 / ForeignKey는 참조하는 값과 동일한 타입으로 만들어줘야 한다.
    question = db.relationship('Question', backref=db.backref('answer_set'))    # Question 테이블과 관계를 가진다. backref = 참조 명칭. 어떤 질문에 해당하는 객체가 a_question일 때, a_question.answer_set과 같은 코드로 해당 질문에 달린 답변들을 참조할 수 있다.
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    # 실제 파이썬 코드에서 질문을 삭제할 때 답변까지 모두 삭제하려면 아래 코드가 추가로 필요하다.
    # question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)   # 그러나 이미 있던 데이터에는 user_id 값이 없다. nullable을 False로 해두면 오류가 난다. server_default는 null 대신 임의의 값을 넣어준다. server_default를 사용하면 flask db upgrade 명령을 수행할 때 null이던 데이터에도 기본값이 저장된다. default를 새로 생성되는 데이터에만 기본값을 생성해준다.
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))


# user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)