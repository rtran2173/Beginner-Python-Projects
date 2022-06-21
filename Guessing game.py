import random

# Define a function
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess again, number is too low")
        elif guess > random_number:
            print("Guess again, number is too high")

    print(f"You guessed correctly, your number is {random_number}.")

# Computer is guessing
def ai(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high

        feedback = input(f"Is {guess} too high(h), or too low(l), or correct(c)?").lower()
        if feedback == "h":
            high == guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Computer guessed right. Your number is {guess}.")

guess(10)
ai(4)

