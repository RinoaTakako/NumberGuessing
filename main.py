import random

# import random library to generate random number 

x = random.randint(1,10)
print(x)

# Ask the user for their input

def get_user_guess():
  return int(input("Please input a number between 1 and 10: "))
  
# Start and play game!

def play_game():
  correct_number = x
  attempts = 0
  
  
  while True:
    user_input = get_user_guess()
    if user_input == correct_number:
  
      attempts += 1
      print(f"Correct Guess! It took you {attempts} tries to get the correct number.")
      break

    elif user_input > correct_number:
      attempts += 1 
      print(f"Incorrect guess! You have tried {attempts} number of guesses. Try lower next time.")
      
    elif user_input < correct_number:
      attempts +=1 
      print(f"Incorrect guess! You have tried {attempts} number of guesses. Try higher next time.")
    
play_game()