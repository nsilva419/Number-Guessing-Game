from random import randint

while True:
    guess = 0
    tries = 0

    print("\n\t\t\tWelcome to the Number Guessing game!\n\nStart by entering a minimum and maximum number.")

    while True:
        try:
            min_number = int(input("Enter minimum number: "))
            break
        except ValueError:
            print("\nInvalid input. Please enter a number.")

    while True:
        try:
            max_number = int(input("Enter maximum number: "))
            if max_number <= min_number:
                print(f"\nMaximum number must be greater than {min_number}. Try again.")
            else:
                break
        except ValueError:
            print("\nInvalid input. Please enter a number.")

    while True:
        try:
            tries_number = int(input("\nHow many tries would you like to have?\nEnter amount of tries: "))
            if tries_number < 1:
                print("\nMust have at least 1 try.")
            else:
                break
        except ValueError:
            print("\nInvalid input. Please enter a number.")


    number = randint(min_number, max_number)


    while guess != number:

        try:
            guess = int(input("\nWhat is your guess? \n"))
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue

        if guess < min_number or guess > max_number:
            print(f"\nInvalid input. Enter a guess between {min_number} and {max_number}.")
            continue

        tries += 1
        print(f"You Guessed {guess}.\nNumber of tries {tries}.")

        if guess > number:
            print("\nToo High, Try Again!")

        elif guess < number:
            print("\nToo Low, Try Again!")


        if tries >= tries_number and guess != number:
            print(f"\nSorry, You've exceeded the max number of tries which is {tries_number}. The number was {number}.")
            break

    if guess==number: 
        print(f"\nYou Guessed {guess}, the number was {number}.\nCongratulations! You Guessed it!")
        print(f"It took you {tries} tries to get it right!")

    play_again = input("\nWould you like to play again? y/n: ").lower()

    if play_again != "y":
        print("\nThanks for playing!")
        break