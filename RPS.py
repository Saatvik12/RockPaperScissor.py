import random
list1 = [1,2,3]
PlayerPoint = 0
AIPoint = 0
Draws = 0
print('Welcome to rock, paper & scissers. You will now be playing against an AI.')
print('')
print('what would you like to choose')
print('')
print('enter "R" for rock')
print('enter "P" for paper')
print('enter "S" for scissors')
for i in range (0,3):

    UserChoice = str(input('your choice: '))
    AIChoice = random.choice(list1)
    if AIChoice == 1:
        print('AI choice is rock')
    elif AIChoice == 2:
        print('AI choice is paper')
    elif AIChoice == 3:
        print('AI choice is scissors')
    print('')
    if AIChoice == 1 and UserChoice == 'R':
        print('You and AI chose the same action')
        print('this round is a draw')
        Draws = Draws + 1
    elif AIChoice == 1 and UserChoice == 'P':
        print('Paper beats rock')
        print('one point to you')
        PlayerPoint = PlayerPoint +1
    elif AIChoice == 1 and UserChoice == 'S':
        print('Rock beat scissors')
        print('one point to AI')
        AIPoint = AIPoint + 1
    elif AIChoice == 2 and UserChoice == 'R':
        print('Paper beats rock')
        print('one point to AI')
        AIPoint = AIPoint +1
    elif AIChoice == 2 and UserChoice == 'P':
        print('You and AI chose the same action')
        print('this round is a draw')
        Draws = Draws + 1
    elif AIChoice == 2 and UserChoice == 'S':
        print('Scissors beat paper')
        print('one point to you')
        PlayerPoint = PlayerPoint +1
    elif AIChoice == 3 and UserChoice == 'R':
        print('Rock beats Scissors')
        print('one point to you')
        PlayerPoint = PlayerPoint +1
    elif AIChoice == 3 and UserChoice == 'P':
        print('Scissors beat paper')
        print('one point to you')
        AIPoint = AIPoint +1
    elif AIChoice == 3 and UserChoice == 'S':
        print('You and AI chose the same action')
        print('this round is a draw')
        Draws = Draws + 1
    print('')
    print('Point Standings:')
    print('You: ', PlayerPoint)
    print('AI: ', AIPoint)
    print('Draws: ', Draws)
    print('')
print('')
print('')
print('GAME OVER!!')
if AIPoint>PlayerPoint:
    print('AI has won!')
elif PlayerPoint>AIPoint:
    print('You have won!')
elif PlayerPoint == AIPoint:
    print("it's a draw :(")

        
    
