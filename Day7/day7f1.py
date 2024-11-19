import random
wordlist = ['agriculture', 'language', 'country', 'state', 'zip', 'association', 'bananas', 'clown']


word = random.choice(wordlist)
print (word)


placeholder = ""

for i in range(len(word)):
    placeholder += "_"

print(placeholder)
  
display = ""
correct_letters = []
gameover = False
while gameover != True:
    guess = input("Guess a letter").lower()

    for i in word:
        if i == guess:
             
            correct_letters.append(guess)
        
        elif i in correct_letters:
            display += i
        else:
            display += "_"
        
    print(display)
    
    
    if display == word:
        print("Congratulations, you guessed the word!")
        gameover = True 