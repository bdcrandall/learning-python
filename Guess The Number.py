import random
min_number=1
max_number=100
number = random.randint(min_number,max_number)
number_of_guesses = 0
max_guesses = 5
guesses_left = (max_guesses - number_of_guesses)
while (number_of_guesses < max_guesses):
    guesses_left = (max_guesses - number_of_guesses) 
    if guesses_left == 1:
        print (f"Guess a number between {min_number} and {max_number}. You have {guesses_left} guess left!")
    else:
        print (f"Guess a number between {min_number} and {max_number}. You have {guesses_left} guesses left!")
    guess = input()
    guess = int(guess)
    if guess>number:
        print ("your guess is too high!")
    elif guess<number:
        print ("your guess is too low!")
    number_of_guesses+=1
    if guess == number:
        print(f"You Win!!! You got it right in {number_of_guesses} guesses")
        break
if guess != number:
    print (f"You Lose!!! The number was {number}")
