import random
def game():
    mode_of_game = input("Choose a difficulty . Type 'easy' or 'hard': ").lower()
    if mode_of_game == 'easy':
        numbers_of_attempt = 10
    else:
        numbers_of_attempt = 5
    got_it = False
    num = random.randint(1, 100)

    while not got_it and numbers_of_attempt>0 :
        print(f"You have {numbers_of_attempt} attempts remaining to guess the number")
        left=int(input("Guess again  : "))
        if left==num:
            print("you got it ")
            got_it=True
        elif numbers_of_attempt==1:
            print("you've run out of guesses , you lose.")
            got_it=True
        elif left>num:
            print("To high !")
        else:
            print("To low !")
        numbers_of_attempt-=1
        if numbers_of_attempt==0:
            print("you reach the attempt you lose")

game()



