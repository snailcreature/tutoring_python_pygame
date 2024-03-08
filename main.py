from random import randint

my_number = randint(1, 10)

your_guess = 0

while (your_guess != my_number):
    your_guess = int(input("What number am I thinking of? "))

    if your_guess == my_number:
        print("Well done! You guessed it!")
    elif your_guess > my_number:
        print("It's smaller than that...")
    else:
        print("It's larger than that!")
