# module for generating random numbers
import random

# constants
min_number = 1
max_number = 10
spook_distance = 3
max_hop_size = 7

# initialize variables
number_of_guesses = 0
max_guesses = 20

# place the rabbit
rabbit = random.randint(min_number,max_number)

# gameplay loop: play until guess limit is reaches or rabbit is caught
while (number_of_guesses < max_guesses):
    # calculate remaining guesses
    guesses_left = (max_guesses - number_of_guesses)

    # print message for user to enter their guess
    if guesses_left == 1:
        print (f"Guess a number between {min_number} and {max_number}. You have {guesses_left} more chance left to catch the rabbit!")
    else:
        print (f"Guess a number between {min_number} and {max_number}. You have {guesses_left} chances left to catch the rabbit!")

    # get user guess
    guess = input()
    # convert guess to integer type
    guess = int(guess)
    # track number of guesses made
    number_of_guesses += 1
    if guess == rabbit:
        # rabbit is caught
        print(f"You Win!!! You caught him in {number_of_guesses} tries")
        break
    if guess < rabbit and guess > rabbit - spook_distance:
        # close to rabbit (below): it hops away
        print ("You spooked it!!! The rabbit ran away to a higher number!")
        hop = random.randint(1, max_hop_size)
        rabbit = min(rabbit + hop, max_number)
    elif guess > rabbit and guess < rabbit + spook_distance:
        # close to rabbit (above): it hops away
        print ("You spooked it!!! The rabbit ran away to a lower number!")
        hop = random.randint(1, max_hop_size)
        rabbit = max(rabbit - hop, min_number)
    elif guess > rabbit:
        print ("Your guess is too high!")
    elif guess < rabbit:
        print ("Your guess is too low!")

# max guesses reached without catching the rabbit
if guess != rabbit:
    print (f"You Lose!!! The rabbit was at {rabbit}")
