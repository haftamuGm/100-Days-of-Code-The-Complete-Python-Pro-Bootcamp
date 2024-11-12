# password generator
import random
letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
password=[]
print("Welcome To The Password Generator")
letter=int(input("How Many Letters Would You Like in Your Password\n"))
symbol=int(input("How Many Symbols Would You Like ? \n"))
number=int(input("How Many Numbers would You Like ?\n"))
for i in range(letter):
    password.append(random.choice(letters))
for j in range(symbol):
    password.append(random.choice(symbols))
for k in range(number):
    password.append(random.choice(numbers))
print(password)
random.shuffle(password)
print(password)
print(f"Your PassWord is : {''.join(map(str,password))}")


