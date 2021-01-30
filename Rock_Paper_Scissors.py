import random as rnd 

print("\nThis is a small game of 'Rock,Paper,Scissors'. Lets's see if you can defeat the AI.\n")
wins = {'scissors':'paper','paper':'rock','rock':'scissors'}
AI = ['rock','scissors','paper']

AI_wins = 0
Player_wins = 0

rounds = int(input("Enter the number of rounds you want to play : "))

for i in range(rounds):
    print("\nRound",i+1)
    move_player = input("Enter your move (rock,paper,scissors) :\n\n")
    index = rnd.randint(0,2)
    move_AI = AI[index]
    print()
    print(move_AI)
    print()
    if wins.get(move_AI) == move_player:
        print("You lost this round.\n")
        AI_wins += 1
    elif wins.get(move_player) == move_AI :
        print("You won this round.\n")
        Player_wins += 1
    else:
        print("This round is tied.\n")

print("\nPlayer : ",Player_wins)
print("\nAI : ",AI_wins)
print()
if AI_wins > Player_wins:
    print("You lost the game. Better luck next time.\n")
elif Player_wins > AI_wins:
    print("You won the game. Congratulations !!! ")
else:
    print("This game is tied.")