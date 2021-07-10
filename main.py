import random
from images import rock, paper, scissors
images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0 <= user_choice < 3:
  print(images[user_choice])
  computer_choice = random.randint(0, 2)
  print(f"Computer chose:\n{images[computer_choice]}")

  if user_choice == computer_choice:
    print("It's a draw.")
  elif (computer_choice - user_choice == -2) or (computer_choice - user_choice == 1):
    print("You lose.")
  else:
    print("You win!")

else:
  print("Err, wrong choice. Try again!")
