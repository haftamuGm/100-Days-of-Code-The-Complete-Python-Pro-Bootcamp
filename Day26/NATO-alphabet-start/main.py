import pandas as p
d=p.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic={row.letter:row.code for index,row in d.iterrows()}
def generic_phontic():
    user = input("Enter a Word :").upper()
    try:
        list_user_phonetic=[nato_phonetic[i] for i in user]
    except KeyError:
        print("Sorry , Only letter in the  alphabet please.")
        generic_phontic()
    else:
        print(list_user_phonetic)
generic_phontic()
