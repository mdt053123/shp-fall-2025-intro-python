import random

def guess_the_number():
    """
    This function will generate a random number in some range (a, b),
    and prompt the user to guess the number until they get it, and
    print to the user how many guesses it took. No params, no return.
    """
    
    number = random.randint(1, 20) # inclusive of both 1, 20
    guesses = 0
    
    guess = -1 # arbitrary starting value outside range
    
    while guess != number:
        guess = int(input("Enter a number between 1 and 20: "))
        guesses += 1
        
        if guess > number:
            print("Too high, guess again!")
        if guess < number:
            print("Too low, guess again!")
            
        if guesses >= 10:
            print("Too many guesses!")
            break
        
    if guess == number:
        print(f"You got it in {guesses} guesses!")
        
guess_the_number()