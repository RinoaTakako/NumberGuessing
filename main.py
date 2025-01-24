import random

x = random.randint(1,10)
print(x)

def get_user_guess():
  return int(input("Please input a number between 1 and 10: "))
  

def play_game():
  correct_number = x
  attempts = 0
  
  
  while True:
    user_input = get_user_guess()
    if user_input == correct_number:
  
      attempts += 1
      print(f"Correct Guess! It took you {attempts} to get the correct number.")
      break

    else:
      attempts += 1 
      print(f"Incorrect guess! You have tried {attempts} number of guesses.")
    
play_game()