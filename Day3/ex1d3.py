print('welcome to python pizza delivery')
size = input('what size would you like your pizza? s , m , l')
pepperoni = input('would you like some pepperoni in you pizza? Y or N')
extra_cheese= input('would you like some extra cheese in your pizza? Y or N')
bill = 0

if size == "s": 
    bill = 15
    print(" you got a small pizza")

elif size == "m": 
    bill = 20
    print(" you got a medium pizza")

else:
    bill = 25
    print(" you got a large pizza")
    
if pepperoni == "Y":
    bill += 2

if extra_cheese == "Y":
    bill += 3


print(f"Your total bill is {bill}")



