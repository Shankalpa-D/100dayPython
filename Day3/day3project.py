print(' welcome to trasure island')
print('your mission is to find the treasure.')
print('you are at a cross road. where do you want to go?')
choice = input('type "left" or "right"').lower()
if choice == "left":
    choice2 = input('you are at a lake. what do you want to d? swim or wait for a boat: type swim or wait').lower()
    if choice2 == "wait":
        print(' the boat came and took you to the other side of the lake.')
        print(' there are 3 doors infront of you. red blue and yellow.')
        choice3 = input('pick a door: r g y').lower()
        if choice3 == 'r':
            print(' there was a huge fire in the room and you died. Game over.')
            
        elif choice3 == 'y':
            print('A huge trasure chest spawned infornt of you, you win.')
            
        else:
            print('A huge trasure chest spawned infornt of you, you win.')
            print('there was a tiger in the room and you died. Game over')
    
    else:
        print('you got eaten by a monster in the lake. Game Over')
        
        
       
else:
    print('You fell off the map. game over')