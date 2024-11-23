with open("./Input/Names/invited_names.txt") as file:
    names=file.readlines()
with open("./Input/Letters/starting_letter.txt") as f:
    letter=f.read()
    for name in names:
        name=name.strip()
        modify_letter=letter.replace("[names]",name)
        with(open(f"./Output/ReadyToSend/{(name)}.docx",mode='w')) as g:
            g.write(letter)
