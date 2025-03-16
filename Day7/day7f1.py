import random

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
game_over = False
display = ""
list = []

word_length = len(chosen_word)
for i in range(word_length): 
    placeholder += "_"
  
print(placeholder)

while not game_over:
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter
            list.append(guess)
        elif letter in list:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        print("Congratulations! You've won the game!")
    game_over = True
print(display)
    
    
 