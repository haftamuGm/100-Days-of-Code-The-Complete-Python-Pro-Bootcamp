from hangman_art import hangman_logo,stages
from hangman_word import words_list
import random
word=random.choice(words_list)
print(hangman_logo)
print(word)
lives=6
correct_letter=[]
print(f"Words To Guess:{'_'*len(word)}")
Game_over=False
while not Game_over:
    print(f"*************************************{lives}/6LIVES LEFT **********************************")
    user=input("Guess a Letter :").lower()
    display=''
    if user in word:
        print("you guess")
    for i in word:
        if i==user:
            display+=i
            correct_letter.append(i)
        elif i in correct_letter:
            display+=i
        else:
            display+='_'

    if user not in word:
        print(f"You Guessed {user}, that's not in word . you lose life")
        lives -= 1
        print(stages[lives])
        if lives==0:
            Game_over=True
            print("***********************IT WAS buffalo! YOU LOSE**********************")
    if '_'  in word:
        Game_over=True

    print(f"Word to Guess : {display}")
    print(f"Guess a Letter :{user}")


