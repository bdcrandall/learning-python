import random
min_number=1
max_number=100
number = random.randint(min_number,max_number)
number_of_guesses = 0
max_guesses = 20
guesses_left = (max_guesses - number_of_guesses)
while (number_of_guesses < max_guesses):
    guesses_left = (max_guesses - number_of_guesses)
    if guesses_left == 1:
        print (f"Guess a number between {min_number} and {max_number}. You have {guesses_left} more chance left to catch the rabbit!")
    else:
        print (f"Guess a number between {min_number} and {max_number}. You have {guesses_left} chances left to catch the rabbit!")
    guess = input()
    guess = int(guess)
    if guess + 1 == number:
        number = random.randint(number,max_number)
        print ("Oh No!!! the rabbit ran away to a higher number!")
    elif guess - 1 == number:
        number = random.randint(min_number,number)
        print ("Oh No!!! the rabbit ran away to a lower number!")
    elif guess > number + 1:
        print ("your guess is too high!")
    elif guess < number - 1:
        print ("your guess is too low!")
    number_of_guesses+=1
    if guess == number:
        print(f"You Win!!! You got it right in {number_of_guesses} guesses")
        break
if guess != number:
    print (f"You Lose!!! The number was {number}")
