from random import choice    #this is needed to add the random functionality to python

def scary_movie_bot(user_response):     #this is the bot's function, basically the brain of the bot where all the thinking and randomization happens

  bot_response_supernatural = ["It's all fake! Watch a behind the scenes video!", "Go watch some peppa pig!"]
  bot_response_thriller = ["Stop watching thrillers! Pingu is a much more entertaining show", "The chances of that ever happenning to you is right around 0", "Go watch an episode of spongebob!"]

  if user_response == "supernatural":       #these if-elif-else statements are selected based on the user's input, in this case either supernatural or thriller
    return choice(bot_response_supernatural)
  elif user_response == "thriller":
    return choice(bot_response_thriller)
  else:
    return "I'm sorry, I can only give advice on recovery from supernatural or thriller horror movies."



print("Welcome to the scary movie recovery system")     #the welcoming statement upon opening the program
print("Was the horror movie you watch supernatural or a thriller?")     #the prompt that requests an input

user_response = ""
while True:     #boolean while loop, program will restart and run again unless the user inputs exit
  user_response = input("Was the horror movie you watch supernatural or a thriller?")
  
  if user_response == 'exit':
    break

  
  bot_response = scary_movie_bot(user_response)     #this defines the bot's answer as the return in the function
  print(bot_response)       #this prints out the result of the bot's randomization based on user input
