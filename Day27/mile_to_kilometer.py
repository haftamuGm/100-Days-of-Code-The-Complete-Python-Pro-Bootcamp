from tkinter import*
window=Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=100,height=50)
window.config(padx=100,pady=100)
user=Entry(width=5)
user.grid(row=0, column=1)
MIle=Label(text="Mile")
MIle.grid(row=0, column=2)
isequal=Label(text="Is Equal ")
isequal.grid(row=1,column=0)
my_text=Label(text="0")
my_text.grid(row=1,column=1)
km=Label(text="KM")
km.grid(row=1,column=2)
def cal():
    my_text.config(text=int(int(user.get()) * 1.60934))

mile_to_kilometer=Button(text="Calculate",command=cal)
mile_to_kilometer.grid(row=2,column=1)

window.mainloop()
