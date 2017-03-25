import indicoio
from pprint import pprint

indicoio.config.api_key = '426cd40e597f61242dba879063d99567'

def get_emotion():
	user_input = input("What are you thinking about right now?")
	print "Ok, you're thinking about " + str(user_input)
	emotion = indicoio.emotion(user_input)
	print emotion


def q1():
	user_input = input("My idea of a fun friday night is ___")
	print "Your input: " + str(user_input)
	emotion = indicoio.emotion(user_input)
	personality = indicoio.personality(user_input)
	personas = indicoio.personas(user_input)

	pprint(emotion)
	e_max = max(emotion, key=emotion.get)
	personas_max = max(personas, key=personas.get)
	personality_max = max(personality, key=personality.get)

	print "Congradulations, your emotion is " + str(e_max) + ", your personality is " + str(personality_max) + ", and your persona is " + str(personas_max)
#results = indicoio.fer("/Users/alex/sc-photo1_crop.jpg")

if __name__ == '__main__':
	q1()
