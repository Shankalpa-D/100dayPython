print('Hello world' [0])
#prints the first letter on the string - subscript

print('Hello world' [-1])
# last letter on the string 

print(type('helloop'))
# prints the type of variable it is - typechecking

#converting datatypes - typecasting 

print(int("123"))

username = input("Username:")
lengthofname = len(username)
new = str(lengthofname)
print (" number of letter in your name is : "+ new)



#mathmath operations - Follws PEMDAS

print ( 6/3) # gives a float value by default
print (6// 3)# gives a int value whrn modifieed by double //
print (2 ** 3) # 2 to the power of 3


# round function 

bmi = 84/1.65 ** 2
print (bmi)
print (int(bmi)) # just floors the number not round 
print(round(bmi)) # whole number round 
print(round(bmi , 2)) # rounds to the 2 number 


# assingment operation
score = 0 
# user scores a point 
score += 1
print (score) 

# f strings 
print( ' your score is '+ str(score))

heigh = 1.8 
is_winning = True 

print(f'the score is {score} and your height is {heigh}')
