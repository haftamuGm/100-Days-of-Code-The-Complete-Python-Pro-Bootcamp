import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
user=int(input("What Do You Choose Type 0 For Rock , 1 for Paper,2 for scissors\n"))
computer=random.randint(0,2)
print("Computer Chose\n")
print(game[computer])
if user>3 or user<0:
    print("Invalid number")
else:
    print(game[user])
    if user == 1 and computer == 0:
        print("You Win")
    elif user == 2 and computer == 1:
        print("You Win")
    elif user == 0 and computer == 2:
        print("You Win")
    elif user == computer:
        print("Its Draw")
    else:
        print("You lose")


