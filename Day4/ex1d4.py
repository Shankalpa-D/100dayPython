import random
from turtledemo.penrose import start

from my_module import my_fav_number

print(random.randint(1, 10))
print(my_fav_number)

random_number = random.random() * 10
print(random_number)

random_float = random.uniform(1, 10)
print(random_float)

headsortails = random.randint(0,1)
if headsortails == 0:
    print('heads')

else:
    print('tails')

    #lists

states_of_america = ['new york', ' jearsey' ,  ' georgia' , ' delaware' , 'pensylvanya']
print(states_of_america)
print(states_of_america[0])
states_of_america[-1] = "north carolina"
print( states_of_america)
states_of_america.append("south carolina") # adds to the last element
print (states_of_america)
states_of_america.extend(["wasingthon", " ohio"]) # adds this new list to the previous list extending it
print(states_of_america)


