# This is the guess the number game
import random
print("Hello, What's your name?")
name = input()
secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinkng a number between 1 and 20.')

# Ask the player to guess the number six times
for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break  # This condition is the correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You took ' + str(guessesTaken) + ' guesses')
else:
    print('Nope! The number I was thinking of was ' + str(secretNumber))
