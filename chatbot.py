from random import choice

def scary_movie_bot(user_response):

  bot_response_supernatural = ["It's all fake! Watch a behind the scenes video!", "Go watch some peppa pig!"]
  bot_response_thriller = ["Stop watching thrillers! Pingu is a much more entertaining show", "The chances of that ever happenning to you is right around 0", "Go watch an episode of spongebob!"]

  if user_response == "supernatural":
    return choice(bot_response_supernatural)
  elif user_response == "thriller":
    return choice(bot_response_thriller)
  else:
    return "I'm sorry, I can only give advice on recovery from supernatural or thriller horror movies."



print("Welcome to the scary movie recovery system")
print("Was the horror movie you watch supernatural or a thriller?")

user_response = ""
while True:
  user_response = input("Was the horror movie you watch supernatural or a thriller?")
  
  if user_response == 'exit':
    break

  
  bot_response = scary_movie_bot(user_response)
  print(bot_response)
