from tkinter import*
import timer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps=0
text="Timer"
color=GREEN
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    mylabel.config(text=text,fg=GREEN)
    canvas.itemconfig(canvas_text,text="00:00")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work=WORK_MIN
    short_break=SHORT_BREAK_MIN
    long_break=LONG_BREAK_MIN
    if reps%8==0:
        count_down(long_break)
        color=PINK
        mylabel.config(text="Break")
        mylabel.config(fg=PINK)
    elif reps%2==0:
        count_down(short_break)
        color=RED
        mylabel.config(text="Break")
        mylabel.config(fg=color)
    else:
        count_down(work)
        color=GREEN
        mylabel.config(text="Work")
        mylabel.config(fg=color)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    min=count // 60
    second=count % 60

    if second<10:
        second=f"0{second}"
    canvas.itemconfig(canvas_text,text=f"{min}:{second}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2==0:
            checkmark.config(text="✔")
        else:
            checkmark.config(text=" ")



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()

window.config(padx=100,pady=50,bg=YELLOW)



mylabel=Label(text=text,font=(FONT_NAME,24,"bold"),fg=color,bg=YELLOW)
mylabel.grid(row=0,column=2)
window.title("Pomodoro")
canvas=Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
image_name=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=image_name)
canvas_text=canvas.create_text(100,132,text="00:00",fill="green",font=(FONT_NAME,24,"bold"))

canvas.grid(row=1,column=2)
start=Button(width=5, text="Start", command=start_timer)
start.grid(row=2,column=0)
checkmark=Label(text="",bg=YELLOW, fg=GREEN, width=3, height=1)
checkmark.grid(row=3, column=2)
reset=Button(width=5,text="Reset",command=timer_reset)
reset.grid(row=2,column=3)


window.mainloop()