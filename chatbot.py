from random import choice

def scary_movie_bot(user_response):

  bot_response_supernatural = ["It's all fake!", "Watch a behind the scenes video!", "I love to see you happy!"]
  bot_response_thriller = ["you are in a safe place!", "sending good vibes"]

  if user_response == "supernatural":
    return choice(bot_response_supernatural)
  elif user_response == "thriller":
    return choice(bot_response_thriller)
  else:
    return "I'm sorry, I can only give advice on recovery from supernatural or thriller horror movies."



print("Welcome to the scary movie recovery system"
print("Was the horror movie you watch supernatural or a thriller?")

user_response = ""
while True:
  user_response = input("Was the horror movie you watch supernatural or a thriller?")
  
  if user_response == 'done':
    break

  
  bot_response = get_mood_bot_response(user_response)
  print(bot_response)
