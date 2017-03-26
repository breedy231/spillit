from spillit.models import User
from config import db_session

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

