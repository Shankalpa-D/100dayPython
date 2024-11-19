import random


print('lets  play rock, paper, sizzors?')
choice = input("make your choice: ").lower()

compchoice = random.randint(1,3)

if ( choice ==  "rock" and compchoice == 1 or choice == 'paper' and compchoice == 2 or choice == 'sizzors' and compchoice == 3 ):
    print('tie')

elif( choice ==  "rock" and compchoice == 2 or choice == 'paper' and compchoice == 3 or choice == 'sizzors' and compchoice == 1 ):
    print(' you lose')

else:
    print('you win')




