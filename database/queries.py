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
    type = randomQuestion.type_id
    questionType = db_session.query(QuestionType).get(randomQuestion.type_id);
    return [randomQuestion.name, questionType.name];

def handle_new_response(response):
    print("recording response" + str(response));
    newResponse = Response(response[0], response[1], response[2]);

    db_session.add(newResponse);
    db_session.commit();

#INCIDIOIO USAGE:

import indicoio
from pprint import pprint

indicoio.config.api_key = '426cd40e597f61242dba879063d99567'

def get_user_emotion(userId):
    r = []
    userResponses = Response.query.filter(Response.user_id == userId);
    for response in userResponses:
        r.append(process_response(response))
    return r;
    #userResponses = Response.query.filter(Response.).count() == 1

def process_response(response):
    print(str(response));
    questionType = response.question_id;
    #questionType = Question.query.get(response.question_id);
    #print(str(question));
    #questionType = QuestionType.query.get(question.type_id);
    print("processing a " +str(questionType));
    result = {};
    user_input = response.response_text;
    if(questionType == "Personality"):
        result = indicoio.personality(user_input);
    elif(questionType == "Emotion"):
        result = indicoio.emotion(user_input);
    elif(questionType == "Persona"):
        result = indicoio.personas(user_input);
    pprint(result)
    max_result = max(result, key=result.get);
    print("max response: " + max_result);
    return "" + max_result;


if __name__ == '__main__':
	q1()
