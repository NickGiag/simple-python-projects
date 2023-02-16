import random
randomNumber = random.randint(1,100)

print("Try to guess the number from 1 to 100!")

while True:
    guess = int(input())

    if guess == randomNumber:
        print("The random number is " + str(randomNumber) + " you guessed right!")
        break
    elif guess < randomNumber:
        print("The random number is higher than the one you guessed. Try again:")
    else:
        print("The random number is lower than the one you guessed. Try again:")
