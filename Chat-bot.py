from random import choice

def get_mood_bot_response(user_response):


  bot_response_happy = ["omg! great!", "Keep smiling!", "I love to see you happy!","Do Your BEST!", "Maintain it"]
  bot_response_sad = ["im here for you", "sending good vibes", "Don't Stress its just life", "Talk to Someone", "Look At The Stars", "Listen to some music."]
  bot_response_mad = ["chill out buddy", "Take a chill pill", "Get some air", "Have a snack, cant go wrong with those"]
  bot_response_chill = ["Listen to some chill music", "have some food", "good, keep it that way", "Share some coolness with me"]

  if user_response == "happy":
    return choice(bot_response_happy)
  elif user_response == "sad":
    return choice(bot_response_sad)
  elif user_response == "chill":
    return choice(bot_response_chill)
  elif user_response == "mad":
    return choice(bot_response_mad)
  else:
    return "Go have some snacks ! It doesnt matter what mood youre in!"




print("Welcome to Mood Bot")
print("Please enter how you are feeling")

user_response = ""

while True:
  user_response = input("How are you feeling today?: ")
  if user_response == 'done':
    break

  
  bot_response = get_mood_bot_response(user_response)
  print(bot_response)



