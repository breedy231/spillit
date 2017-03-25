import indicoio

indicoio.config.api_key = '426cd40e597f61242dba879063d99567'

def get_emotion():
	user_input = input("What are you thinking about right now?")
	print "Ok, you're thinking about " + str(user_input)
	emotion = indicoio.emotion(user_input)
	print emotion



#results = indicoio.fer("/Users/alex/sc-photo1_crop.jpg")

if __name__ == '__main__':
	get_emotion()
