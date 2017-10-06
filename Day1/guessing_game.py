import random
import emoji

def guess_a_number():

    print (
        '''
        Welcome!!! This is a guessing game.
        You'd choose a number between 1 and 15, 
        if your number is equal to my guess, you won!!! 
        if not, you'd loose after 5 trial :(.
        
        Let's begin.
        '''
    )
    life = 5

    while life > 0 :
        print ("I'm thinking of number between 1 and 15. Guess the number")
        guess = random.randint(1, 30)
        try:
            number = int(input('>> '))
            if number > guess:
                print("Sorry your guess is too high!!" + emoji.emojize(':yum:', use_aliases=True))
                life -= 1
            elif number < guess:
                print("Sorry your guess is too low!! " + emoji.emojize(':yum:', use_aliases=True))
                life -= 1
            else:
                print("Yass!!! You guessed right. Take some cookie " + emoji.emojize(':cookie:', use_aliases=True))
                break

        except:
            print ("I need a number please. Try again!")
            continue

        if life == 0 and guess != number:
            print("You lost :(")
            print("I was thinking of number " + str(guess) + " " + emoji.emojize(':shit:', use_aliases=True))

guess_a_number()