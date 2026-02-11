'''
============ learnings ============

1. learned about chosing random word from a list
2. learned about joining the elements of list by using " .join() " function
3. learned better way to apply boolean logic

'''

import random   

#initialization
word_list = ["Rabbit", "Eagle", "Sparrow", "Snake"]
display = []
lives = 6
guessed_letters = []
stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]


chosen_word = random.choice(word_list).lower()    #  choosing random word

for letter in chosen_word:    #  making required blanks for words
    display.append("_")

print(stages[0])
print (" ".join(display))    #  better visual view for blanks

while lives > 0:    #  main loop
    guess = input("Guess a letter : ").lower()

    if guess in guessed_letters:    #  case for already guessed letter
        print (f"Already guessed {guess}")
        continue

    guessed_letters.append(guess)    #  storing guessed letters for memory

    found = False

    for letter in range(len(chosen_word)):    #  filling the blanks with correct letter(s)
        if chosen_word[letter] == guess:
            display[letter] = guess
            found = True
    
    if not found:    #  deducting lives for incorrect answer
        lives -= 1
        print (f"Wrong answer, lives left : {lives}")       
        print (stages[6 - lives])

    print (" ".join(display))

    if "_" not in display:    #  winning case
        print ("You Win!")
        break

    if lives == 0:    #  losing case
        print ("Game Over!")
        break

print ("Word was :", chosen_word.capitalize())    #  showing the real word