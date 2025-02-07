import tkinter as tk
from threading import Timer


class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text App")
        self.root.geometry("500x300")

        self.text_widget = tk.Text(root, font=("Arial", 14), wrap="word")
        self.text_widget.pack(expand=True, fill="both", padx=10, pady=10)

        self.text_widget.bind("<KeyPress>", self.reset_timer)

        self.timer = None
        self.start_timer()

    def start_timer(self):
        self.timer = Timer(5, self.clear_text)
        self.timer.start()

    def reset_timer(self, event=None):
        if self.timer:
            self.timer.cancel()
        self.start_timer()

    def clear_text(self):
        self.text_widget.delete("1.0", tk.END)
        self.start_timer()


if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextApp(root)
    root.mainloop()
