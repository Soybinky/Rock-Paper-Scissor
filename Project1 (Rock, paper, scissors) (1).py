#Aaron Ngo
#ITP 100
#================================================================================
import random
#Create scores for computer and player. Also counter for loop
player_score = 0
computer_score = 0
count = 0
#Create variable that user can input for game
name = input('Enter Your Name: ')
#Create while loop
while (count < 5):
#Create the main function for rock,paper,scissors
#Create line that prints the Winner of each round
#Create line that prints tie
    player_choice = int(input('Enter 1 for rock, 2 for paper, and 3 for scissors: '))
#Created a line that picks a random number from 1, 2, or 3
    computer_choice = random.randint(1, 3)
#Main function
    if player_choice == computer_choice:
        print("It's a Tie!")
#==================================================================================
#If player picks rock
    elif player_choice == 1:
        if computer_choice == 2:
            print("Paper wraps rock! Computer wins!")
            computer_score += 1
            print("computer score: " + str(computer_score) + "\n" + "your score:" + str(player_score))

        if computer_choice == 3:
            print("Rock smashes scissors! " + name + " wins!")
            player_score += 1
            print("computer score: " + str(computer_score) + "\n" + "your score:" + str(player_score))
#If player picks paper
    elif player_choice == 2:
        if computer_choice == 1:
            print("Paper wraps rock! " + name + " wins!")
            player_score += 1
            print("computer score: " + str(computer_score) + "\n" + "your score:" + str(player_score))

        if computer_choice == 3:
            print("Scissors cuts paper! Computer wins!")
            computer_score += 1
            print("computer score: " + str(computer_score) + "\n" + "your score:" + str(player_score))
#If player picks scissors
    elif player_choice == 3:
        if computer_choice == 1:
            print("Rock smashes scissors! Computer wins!")
            computer_score += 1
            print("computer score: " + str(computer_score) + "\n" + "your score:" + str(player_score))

        if computer_choice == 2:
            print("Scissor cuts paper! " + name + " wins!")
            player_score += 1
            print("computer score: " + str(computer_score) + "\n" + "your score:" + str(player_score))
#======================================================================================================
#Create input that allows user to continue or not
#Create line that adds 1 to counter
    if input("Do You Want to Continue? Y/N  ") == "Y":
        pass
    else:
        break

    count +=1
