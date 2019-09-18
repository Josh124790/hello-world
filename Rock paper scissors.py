import time
from random import randint
plays = ['rock', 'paper', 'scissors']
playing = False
chosen = False
print('loading.')
time.sleep(0.5)
print('loading..')
time.sleep(0.5)
print('loading...')
time.sleep(0.5)
print('Hello and welcome to Rock Paper scissors')

while playing == False:
    
    start = input('would you like to play Yes or No')
    start = start.lower()
    start = start.strip()
    
    if start == ('no'):
        print('Ok bye')
        time.sleep(2)
        exit()
        playing = False
    
    elif start == ('yes'):
        playing = True

    else:
        print('sorry i did not get that')
        playing = False

playing_again = ('yes')

while playing_again == ('yes'):
    playing_again = ('no')

    computer = plays[randint(0,2)]

    while chosen == False:
        player = input('Ok, type Rock, Paper or Scissors')
        player = player.lower()
        player = player.strip()
        
        if player == plays[0] or plays[1] or plays[2]:
            print('Good choice')
            time.sleep(1)
            chosen = True 
        else:
            print('Sorry type that again please')
            chosen = False

    if player == computer:
        print('Tie')

    elif player =='rock':
        
        if computer == 'paper':
            print('You lose computer covers player')
            
        else:
            print('You win player enialates computer')
            
    elif player == 'paper':
        
        if computer == 'scissors':
            print('you lose computer cuts player')
            
        else:
            print('you win player covers computer')
            
    elif player == 'scissors':

        if computer == 'rock':
            print('You lose computer smashes player')
            
        else:
            print('You win player cuts player')

    playing_2 = False
    while playing_2 == False:
        playing_again = input('Do you want to play again? Yes or No')
        playing_again = playing_again.lower()
        playing_again = playing_again.strip()
        
        if playing_again == ('no'):
            print('Ok bye')
            time.sleep(2)
            playing_2 = False
            exit()
            
            
        elif playing_again == ('yes'):
            chosen = False
            playing_2 = True

        else:
            print('sorry i did not get that')
            playing_2 = False

        
