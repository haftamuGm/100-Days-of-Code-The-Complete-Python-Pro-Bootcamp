import pandas as p
d=p.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic={row.letter:row.code for index,row in d.iterrows()}
user=input("Enter a Word :").upper()
list_user_phonetic=[]
for i in user:
    list_user_phonetic.append(nato_phonetic[i])
print(list_user_phonetic)
