import random
import time
#Rock = 1 Scissors = 2 Paper = 3



def game():
    won = False
    while won == False:
        pcturn = random.randint(1, 3)
        player = (input('Rock paper scissors '))
        player = player.upper()
        while player == 'ROCK':
            if pcturn == 2:
                print('You chose Rock')
                time.sleep(2)
                print('Pc chose Scissors!')
                time.sleep(1)
                print('You win!')
                won = True
                break
            elif pcturn == 3:
                print('You chose Rock')
                time.sleep(2)
                print('Pc chose paper!')
                time.sleep(1)
                print('You lose!')
                player = ''

            else:
                print('You chose Rock')
                time.sleep(2)
                print('Pc chose Rock!')
                time.sleep(1)
                print('Draw!')
                player = ''
        while player == 'PAPER':
            if pcturn == 1:
                print('You chose Paper')
                time.sleep(2)
                print('Pc chose Rock!')
                time.sleep(1)
                print('You win!')
                won = True
                Break
            elif pcturn == 2:
                print('You chose paper')
                time.sleep(2)
                print('Pc chose Scissors!')
                time.sleep(1)
                print('You lose!')
                player = ''
            else:
                print('You chose paper')
                time.sleep(2)
                print('Pc chose paper!')
                time.sleep(1)
                print('Draw!')
                player = ''
        while player == 'SCISSORS':
            if pcturn == 1:
                print('You chose Scissors')
                time.sleep(2)
                print('Pc chose rock!')
                time.sleep(1)
                print('You lose!')
                player = ''
            elif pcturn == 2:
                print('You chose Scissors')
                time.sleep(2)
                print('Pc chose Scissors!')
                time.sleep(1)
                print('Draw!')
                player = ''
            else:
                print('You chose scissors')
                time.sleep(2)
                print('Pc chose paper!')
                time.sleep(1)
                print('You won!')
                won = True
                break



game()
