import random
import string
import time
# Generate a random number between 1 and 5
answer = random.randint(1, 5)

# Ask the player to guess the number
guess = int(input("Guess a number between 1 and 5: "))

# Keep track of the number of guesses
num_guesses = 1

# Keep guessing until the player gets it right
while guess != answer:
  # If the guess is too high, tell the player
  if guess > answer:
    print("Your guess is too high. Try again.")
  # If the guess is too low, tell the player
  else:
    print("Your guess is too low. Try again.")

  # Get the player's next guess
  guess = int(input("Guess a number between 1 and 5: "))
  num_guesses += 1
  # Print a message when the player gets it right
  print(f"Congratulations! You guessed the correct number in {num_guesses} guesses!")