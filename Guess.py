import random

secret_number = random.randint(1, 100)

while True:
    user_input = input("Guess the number (1-100) or 'q' to quit: ")

    if user_input.lower() == "q":
        print(f"Game over! The number was {secret_number}.")
        break

    guess = int(user_input)

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You win!")
        break
