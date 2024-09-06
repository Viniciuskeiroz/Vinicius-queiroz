import tkinter as tk
import datetime

class Clock:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(master, font=('digital-7', 80), fg='green')
        self.label.pack()
        self.update_clock()

    def update_clock(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.master.after(1000, self.update_clock)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("450x150")
root.resizable(False, False)
clock = Clock(root)
root.mainloop()