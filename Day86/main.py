import tkinter as tk
from tkinter import messagebox
import time


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        self.sample_text = "My name is haftamu gebremaryam i'm deep learner"
        self.start_time = None
        self.end_time = None
        self.create_widgets()

    def create_widgets(self):
        self.sample_text_label = tk.Label(self.root, text="Sample Text", font=("Arial", 14))
        self.sample_text_label.pack(pady=10)

        self.text_display = tk.Label(self.root, text=self.sample_text, font=("Arial", 12), wraplength=500)
        self.text_display.pack(pady=10)
        self.input_box = tk.Entry(self.root, font=("Arial", 14), width=50)
        self.input_box.pack(pady=10)
        self.start_button = tk.Button(self.root, text="Start", font=("Arial", 12), command=self.start_test)
        self.start_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def start_test(self):
        self.result_label.config(text="")
        self.input_box.delete(0, tk.END)
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.input_box.bind('<Return>', self.end_test)

    def end_test(self, event=None):
        self.end_time = time.time()
        typed_text = self.input_box.get()
        word_count = len(typed_text.split())

        time_taken = self.end_time - self.start_time
        wpm = (word_count / time_taken) * 60

        self.result_label.config(text=f"Your typing speed is {wpm:.2f} words per minute.")
        self.start_button.config(state=tk.NORMAL)
        if typed_text.strip() == self.sample_text:
            messagebox.showinfo("Congratulations", "You typed the correct text!")
        else:
            messagebox.showwarning("Try Again", "You didn't type the text correctly.")
        self.input_box.unbind('<Return>')

root = tk.Tk()
app = TypingSpeedApp(root)
root.mainloop()
