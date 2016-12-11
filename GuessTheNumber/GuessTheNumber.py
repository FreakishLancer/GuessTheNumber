import random

guessesTaken = 0
stillPlaying = True

print("Hello! What is your name?")
playerName = input()

number = random.randint(1, 20)
print("Well, {0}, I am thinking of a number between 1 and 20.".format(playerName))

while stillPlaying:
    while guessesTaken < 6:
        print("Take a guess, 1-20.")
        guess = input()
        guess = int(guess)

        guessesTaken += 1
    
        if guess < number:
            print("Your guess is too low.")
        if guess > number:
            print("Your guess is too high.")
        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Good job, {0}! You guessed my number in {1} guesses!".format(playerName, guessesTaken))

    if guess != number:
        number = str(number)
        print("Nope. The number I was thinking of was {0}.".format(number))

    guessesTaken = 0

    print("Do you still want to play? Answer 'Y' if yes.")
    if input() != 'Y':
        stillPlaying = False