import random

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
game_over = False
display = ''
list = []

word_length = len(chosen_word)
for i in range(word_length): 
    placeholder += "_"
  
print(placeholder)
while game_over == False:
    guess = input("Guess a letter: ").lower()
    
    display = ''
    for letter in chosen_word:
        if letter == guess:
            display += guess
            list.append(letter)
        elif letter in list:
            display += letter
            
        else:
            display += "_"
            
        if "_" not in display:
            print("Congratulations, you've won!, The word was " + display)
            game_over = True
            
    print(display)
