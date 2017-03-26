from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database.config import Base

class User(Base):
    __tablename__ = 'USER'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    score = Column(Integer)
    leader = Column(Boolean)

    def __init__(self, name=None, leader=False, score=0):
        self.name = name
        self.score = score
        self.leader = leader

    def __repr__(self):
        return "<User '%s'(score='%d', leader='%b')>" % (
            self.name, self.score, self.leader)

class Response(Base):
    __tablename__ = 'RESPONSE'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('USER.id'))
    question_id = Column(Integer, ForeignKey('QUESTION.id'))
    response_text = Column(String(200))

    def __init__(self, user_id=None, question_id=None, response_text=None):
        self.user_id = user_id
        self.question_id = question_id
        self.response_text = response_text

    def __repr__(self):
        return "<User(user id='%d', question id='%d' response text='%s')>" % (
            self.user_id, self.question_id, self.response_text)

class Question(Base):
    __tablename__ = 'QUESTION'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=False)
    type_id = Column(Integer, ForeignKey('QUESTION_TYPE.id'))

    def __init__(self, name=None, type_id=None):
        self.name = name
        self.type_id = type_id

    def __repr__(self):
        return "<Question %s(type id='%s')>" % (
            self.name, self.type_id)

class QuestionType(Base):
    __tablename__ = "QUESTION_TYPE"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Qusetion Type(name='%s')>" % (
            self.name)
