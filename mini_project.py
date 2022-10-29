import random

exit = False
player_points = 0
computer_points = 0

while exit == False:
    options = ["R", "P" , "S"]
    player_input = input("Choose R for rock, P for paper, S for scissors or exit: ").upper()
    computer_input = random.choice(options)
    #player_input.upper()
    print(player_input)
    
    if player_input == "exit" :
        print("Game ended")
        print("You won a total score of "+str(player_points)+" and the computer total score is " +str(computer_points))
        exit = True

    if player_input == "R":
        if computer_input == "R":
            print("Your input is rock")
            print("computer input is rock")
            print("It is a tie!")
        elif computer_input == "P":
            print("Your input is rock")
            print("computer input is paper")
            print(" computer wins")
            computer_points += 1
        elif computer_input == "S":
            print("Your input is rock")
            print("computer input is scissors")
            print("you win")
            player_points += 1

    elif player_input == "P":
        if computer_input == "R":
            print("Your input is paper")
            print("computer input is rock")
            print("you win!")
            player_points += 1
        elif computer_input == "P":
            print("Your input is paper")
            print("computer input is paper")
            print("it's a tie!")
        elif computer_input == "S":
            print("Your input is paper")
            print("computer input is scissors")
            print("computer wins")
            computer_points += 1

    elif player_input == "S":
        if computer_input == "R":
            print("Your input is scissors")
            print("computer input is rock")
            print("computer win!")
            computer_points += 1
        elif computer_input == "P":
            print("Your input is scissors")
            print("computer input is paper")
            print("you win")
            player_points += 1
        elif computer_input == "S":
            print("Your input is scissors")
            print("computer input is scissors")
            print("its a tie")

    elif player_input != " R" or player_input != "P" or player_input != "S":
        print("Invalid Input")