# range funtion with the for loop 

for num in range(1,10):
    print(num)
    
# by default range will increment by 1 and if you want to chanfe that all you have to do is add a coma and another number that you want to be incremented by 
# ex
for n in range(0,100,10):
    print(n)
    
# how to add up all the numbers form 1 - 100 
total = 0 
for numbers in range(1,101):
    total += numbers
    print(total)
       