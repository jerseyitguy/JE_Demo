import random

secret_number = random.randint(1, 100)

while True:
    user_input = input("This is a woderful game Guess the number (1-100) or 'q' to quit: ")

    if user_input.lower() == "q":
        print(f"Game over! The number was {secret_number}.")
        break

    guess = int(user_input)
guess = 0
attempts = 0  # 1. Added a counter for the score

while guess != secret_number:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1  # 2. Add 1 to the counter each time they guess

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You win!")
        break

# 3. Update the win message to show the final score
print(f"You win! It took you {attempts} guesses.")
