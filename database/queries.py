from models import *
import random
import pprint
from database.config import db_session

def handle_new_user(message):
    newUser = User(message);
    if(User.query.filter(User.leader).count() == 1):
        db_session.add(newUser);
    else:
    	newUser.leader = True;
    	db_session.add(newUser);
    db_session.commit();

    return newUser.id;

def handle_new_response(message):
	newResponse = Response()

def retrieve_question():
    questionCount = int(Question.query.count());
    questionNum = int(questionCount*random.random());
    print(questionNum);
    randomQuestion = db_session.query(Question).get(questionNum);
    questionType = db_session.query(QuestionType).get(randomQuestion.type_id);
    return [randomQuestion.name, questionType.name];

def handle_new_response(response):
    print("recording response" + str(response));
    newResponse = Response(response[0], response[1], response[2]);

    db_session.add(newResponse);
    db_session.commit();
