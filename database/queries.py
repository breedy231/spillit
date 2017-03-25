from models import User
from database.config import db_session

def handle_new_user(message):
    newUser = User(message);
    if(User.query.filter(User.leader).count() == 0):
        db_session.add(newUser, True);
    db_session.commit();
