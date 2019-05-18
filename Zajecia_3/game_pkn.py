import random

player_points = 0
computer_points = 0
choice = ["paper", "stone", "nozyczkis"]
rounds = int(input("How many rounds you want to play: "))
print("To play the game you need to choose between: paper, stone and nozyczkis!")
played_round = 1

while(played_round <= rounds):
    if played_round == rounds:
        print("Last round!")
    else:
        print("ROUND " + str(played_round) + "!")

    yt = input("What do you choose?: ")
    ct = random.choice(choice)
    print(ct)
    if yt != None or yt != "paper" or yt != "stone" or yt != "nozyczkis":
        if yt == "paper" and ct == "paper":
            print("Draw!")
            player_points += 1
            computer_points += 1
            played_round += 1
        elif yt == "stone" and ct == "stone":
            player_points += 1
            computer_points += 1
            played_round += 1
            print("Draw!")
        elif yt == "nozyczkis" and ct == "nozyczkis":
            print("Draw!")
            player_points += 1
            computer_points += 1
            played_round += 1

        if yt == "nozyczkis" and ct == "stone":
            print("Point for computer!")
            computer_points += 1
            played_round += 1
        elif yt == "stone" and ct == "paper":
            print("Point for computer!")
            computer_points += 1
            player_points += 1
        elif yt == "paper" and ct == "nozyczkis":
            print("Point for computer!")
            computer_points += 1
            played_round += 1

        if yt == "stone" and ct == "nozyczkis":
            print("Point for you!")
            player_points += 1
            played_round += 1
        elif yt == "paper" and ct == "stone":
            print("Point for you!")
            player_points += 1
            played_round += 1
        elif yt == "nozyczkis" and ct == "paper":
            print("Point for you!")
            player_points += 1
            played_round += 1

        print("Current score is: " + str(player_points) + "-" + str(computer_points) + '\n')

    else:
        print("Wrong value, try stone, nozyczkis or paper!")

if player_points > computer_points:
    print("The winner is Player!!!")
elif player_points < computer_points:
    print("The winner is Computer!!!")
else:
    print("Draw!")
