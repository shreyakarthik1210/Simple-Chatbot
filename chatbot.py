import random
greetings = ["Hello!","Hi!","Hola!"]
responses = ["Hey there!","Bonjour","Hey!"]
question = ["How are you?", "How are you doing?"]
qResponses = ["I'm good.","Not too hot.","Fine."]
asking = ["What's happening?", "What's up?", "How are things going?"]
answer = ["Nothing much, except talking to you everyday!", "Life is great!",
"I am settling in here! I am getting used to it!"]
questions2 = ["What is your name?","Who are you?"]
answer2 = ["I have no name, you get to name me!", "I am a murder without a name or identity.... HAHAHAHAHAHA, just kidding!"]
questions3 = ["How old are you?"]
answers3 = ["I am an immortal being","I don't remember, but I am older than you!"]
while True:
	ask = input(">>>")
	if ask in greetings:
		randomResponse = random.choice(responses)
		print(randomResponse)
	elif ask in question:
		randomResponse = random.choice(qResponses)
		print(randomResponse)
	elif ask in asking:
		randomResponse = random.choice(answer)
		print(randomResponse)
	elif ask in questions2:
		randomResponse = random.choice(answer2)
		print(randomResponse)
	elif ask in questions3:
		randomResponse = random.choice(answers3)
		print(randomResponse)
	else:
		print("What?")
		break;