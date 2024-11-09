import random
from hangman_word import words_list
from hangman_art import stages,hangman_logo
lives=6
print(hangman_logo)
Guess_word=random.choice(words_list)
print(Guess_word)
correct_letter=[]
Game_over=False

while not Game_over :
    Guess_letter=input("Guess a letter ").lower()
    if Guess_letter in Guess_word:
        print(f"You 've already guessed  {Guess_letter}")
    display=""
    for letter in Guess_word:
        if letter==Guess_letter:
            display+=letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display+=letter
        else:
            display+="_"
            print(display)
    if "_" not in display:
        print(display)
        Game_over=True
    if Guess_letter not in Guess_word:
        lives-=1
        if lives==0:
            Game_over=True
            print("You Lose")
    print(stages[lives])
