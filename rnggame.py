#andrew kellmer and parker gowans 11/2/18
import random

mini = 0
maxi = 100
counter = 5
rng = 50
counter1 = 5





#menu
def menu():
    global mini
    global maxi
    global rng    

    choice = input("\nchoose an option play/options/credits/quit:").lower()
    if choice == "play":
        print("starting game...")
        rng = random.randrange(mini, maxi)
        game()
    elif choice == "options":
        print("entering options...")
        options()
    elif choice == "credits":
        print("\nMade by Andrew Kellmer and Parker Gowans.")
        print("Made on 11/2/18")
        menu()
    elif choice == "quit":
        quit1()
    else:
        print("that was not a valid input")
        menu()


#game
def game():
    global counter
    global mini
    global maxi
    global rng
    global counter1
    if counter>0:
        print("\nyou have",counter,"tries left. The range is",mini,"-",maxi,".")
    
        guess = input("enter your guess or quit").lower()

        if guess.isdigit():
            guess = int(guess)
            if guess == rng:
            
                print("\nyou guessed correctly. good job. returning to the menu...")
                menu()
    
            elif guess>=rng and guess<=maxi:
                print("\nyou guessed too high!.")
                counter = counter-1
                game()
        
            elif guess<=rng and guess>=mini:
                print("\nyou guessed too low!.")
                counter = counter-1
                game()

            else:
                print("\nthe value you entered was not in the range.")
                game()
                
        elif guess.isalpha():
            if guess == "quit":
                print("\nquitting the game. returing to menu...")
                menu()
            else:
                print("\nthat was not a valid input")
                game()
            
        else:
            print("\nthat was not a valid input")
            game()

    else:
        print("\nyou have run out of guesses.")
        print("the number was:",rng)
        counter=counter1
        menu()


#options
def options():
    global mini
    global maxi
    global counter
    global counter1

    yn = input("\nwould you like to edit the options y/n:").lower()

    if yn == "y" or yn == "yes":
        print("\nthe default minimum is 0. The minimum cannot be higher than the current maximum.")
        minienter = input("enter a new minimum")
        
        if minienter.isdigit():
            minienter = int(minienter)
            if minienter<maxi:
                print("\nthe new minimum has been set")
                mini = int(minienter)
            else:
                print("\nthe minimum cannot be higher than the current maximum.")
                options()
        else:
            print("\nThat is not a valid input")
            options()
            
        print("\nthe default maximum is 100. The maximum cannot be lower than the current minimum.")
        maxienter = input("enter a new maximum")
        
        if maxienter.isdigit():
            maxienter = int(maxienter)
            if maxienter>mini:
                print("\nthe new maximum has been set")
                maxi = int(maxienter)
            else:
                print("\nthe maximum cannot be higher than the current maximum.")
                options()
        else:
            print("\nThat is not a valid input")
            options()
            
        print("\nthe default counter(number of guesses) is 5")
        counterenter = input("enter a new counter")
        
        if counterenter.isdigit():
            print("\nthe new counter has been set")
            counter = int(counterenter)
            counter1 = int(counterenter)
        else:
            print("\nThat is not a valid input")
            options()
            
        print("\nsettings saved, returning to menu...")
        menu()

    else:
        print("\nThat is not a valid input")
        menu()





#quit
def quit1():
    print("\nyou have quit the game.")
    quit




menu()
