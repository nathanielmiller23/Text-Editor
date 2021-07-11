#Source Code will be on this file
#using Tkinter package

import tkinter as tk

class PyText:
    def _init_(self, master):
        master.title("Untitled - PyText")
        master.geometry("1200x700")



if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()
