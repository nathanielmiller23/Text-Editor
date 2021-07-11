#Source Code will be on this file
#using Tkinter package

import tkinter as tk

class PyText:
    def __init__(self, master):
        master.title("Untitled - PyText")
        master.geometry("1200x700")

        self.textarea = tk.Text(master)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.RIGHT)



if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()