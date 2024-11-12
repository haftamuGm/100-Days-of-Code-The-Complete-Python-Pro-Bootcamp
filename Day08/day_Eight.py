from art import logo
alphapet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
def ceasar(text,shift,encode_decode):
    if encode_decode=='decode':
        shift*=-1
    out_text=''
    for i in text:
        if i not in alphapet:
            out_text+=i
        else:
            position = alphapet.index(i) + shift
            out_text += alphapet[position%len(alphapet)]
    print(f"Here is the {direction} Result {out_text}")
end=False
while not end:
    direction = input("Type 'encode' to encode or Type 'decode' to decode \n ").lower()
    text = input("Type Your Message\n").lower()
    shift = int(input("Type The Shift number \n"))
    ceasar(text, shift, direction)
    # when we want to decode or encode we have to type yes if type no the progam wil end
    user=input("Type 'Yes' if you want to go agin otherwise Type 'No'").lower()
    if user=='no':
        end=True
        print("Good bye")
