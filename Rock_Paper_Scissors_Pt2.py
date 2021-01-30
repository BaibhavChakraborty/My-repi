import random as rnd

print("\nAfter the success of our last contest, it's time to introduce another contest.\nPreviously, it was based on the maximum number of wins out of a certain rounds.\nThis time we will see who scores the required points quickly, for victory.\n\n")
print("Let's see if you can beat the AI this time.\n\n")

wins = {'scissors':'paper','rock':'scissors','paper':'rock'}
AI = ['rock','paper','scissors']

points = int(input("Enter the value of points for which you want to play :\n\n"))
print("\nThe first one to score",points,"points win this game.\n")
player_points = 0
AI_points = 0

while AI_points != points and player_points != points:
    move_player = input("Enter your move (rock,paper,scissors) :\n\n")
    index = rnd.randint(0,2)
    move_AI = AI[index]
    print()
    print(move_AI)
    print()
    if wins.get(move_player) == move_AI:
        player_points += 1
        print("Player : ",player_points)
        print("AI : ",AI_points)
        print()
    elif wins.get(move_AI) == move_player:
        AI_points += 1
        print("AI : ",AI_points)
        print("Player : ",player_points)
        print()
    else:
        if AI_points > player_points:
            print("AI : ",AI_points)
            print("Player : ",player_points)
            print()
        elif player_points > AI_points:
            print("Player : ",player_points)
            print("AI : ",AI_points)
            print()
        else:
            print("Player : ",player_points)
            print("AI : ",AI_points)
            print()

if AI_points == points:
    print("You lost the game. Better luck next time.\n")
else:
    print("Congratulations !!! . You won the game. Keep it up.\n")