from random import choice

def scary_movie_bot(user_response):

  bot_response_happy = ["omg! great!", "Keep smiling!", "I love to see you happy!"]
  bot_response_sad = ["im here for you", "sending good vibes"]

  if user_response == "happy":
    return choice(bot_response_happy)
  elif user_response == "sad":
    return choice(bot_response_sad)
  else:
    return "I hope your day gets better"






print("Welcome to Mood Bot")
print("Please enter how you are feeling")

user_response = ""
while True:
  user_response = input("How are you feeling today?: ")
  
  if user_response == 'done':
    break

  
  bot_response = get_mood_bot_response(user_response)
  print(bot_response)
