from random import randint

while True:
    guess = 0
    tries = 0

    print("\t\t\tWelcome to the Number Guessing game!\nStart by entering a minimum and maximum number.")

    while True:
        try:
            min_number = int(input("Enter minimum number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            max_number = int(input("Enter maximum number: "))
            if max_number <= min_number:
                print(f"Maximum number must be greater than {min_number}. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            tries_number = int(input("How many tries would you like to have?\nEnter amount of tries: "))
            if tries_number < 1:
                print("Must have at least 1 try.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")


    number = randint(min_number, max_number)


    while guess != number:

        try:
            guess = int(input("What is your guess? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < min_number or guess > max_number:
            print(f"Invalid input. Enter a guess between {min_number} and {max_number}.")
            continue

        tries += 1
        print(f"You Guessed {guess}. Number of tries {tries}.")

        if guess > number:
            print("Too High, Try Again!")

        elif guess < number:
            print("Too Low, Try Again!")


        if tries >= tries_number and guess != number:
            print(f"Sorry, You've exceeded the max number of tries which is {tries_number}. The number was {number}.")
            break

    if guess==number: 
        print(f"You Guessed {guess}, the number was {number}.\nCongratulations! You Guessed it!")
        print(f"It took you {tries} tries to get it right!")

    play_again = input("Would you like to play again? y/n: ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break