from  tkinter import *
import pandas
import random
to_dict={}
current_card={}
try:
    data=pandas.read_csv(filepath_or_buffer="data/unkown_word.csv")
except FileNotFoundError:
    orginal=pandas.read_csv("data/french_words.csv")
    to_dict=orginal.to_dict(orient="records")

else:
    to_dict=data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(canvas_text,text="English",fill="white")
    canvas.itemconfig(french_word,text=current_card["English"],fill="white")
    canvas.itemconfig(backround_image,image=back)


def next():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_dict)
    canvas.itemconfig(canvas_text, text="French",fill="black")
    canvas.itemconfig(french_word,text=current_card["French"],fill="black")
    canvas.itemconfig(backround_image,image=front)
    flip_timer=window.after(3000,flip_card)
def is_known():
    to_dict.remove(current_card)
    data=pandas.DataFrame(to_dict)
    data.to_csv("data/unkown_word.csv",index=False)
    print(len(to_dict))
    next()


BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
flip_timer=window.after(3000,flip_card)
window.title(f"{" "*30} Flash Card")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526)
back=PhotoImage(file="images/card_back.png")
front=PhotoImage(file="images/card_front.png")
backround_image=canvas.create_image(400,263,image=back)
left=PhotoImage(file="images/wrong.png")
right=PhotoImage(file="images/right.png")
canvas_text=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
french_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,columnspan=2)
count=0
unknown_button=Button(image=left,command=next)

unknown_button.grid(row=1, column=0)
known_button=Button(image=right,command=is_known)
known_button.grid(row=1,column=1)
next()
window.after(3000, flip_card)
window.mainloop()
