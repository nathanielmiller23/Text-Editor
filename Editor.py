# Source Code will be on this file
# using Tkinter package

import tkinter as tk
from tkinter import filedialog


class Menubar:
    def __init__(self, parent):
        font_specs = ("times new roman", 14)

        self.master = master
        self.filename = None

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File", command=parent.new_file)
        file_dropdown.add_command(label="Open File", command=parent.open_file)
        file_dropdown.add_command(label="Save", command=parent.save)
        file_dropdown.add_command(label="Save As", command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit", command=parent.master.destroy)

        menubar.add_cascade(label="File", menu=file_dropdown)


class MillyText:

    def __init__(self, master):
        master.title("Untitled - MillyText")
        master.geometry("1200x700")

        font_specs = ("times new roman", 16)

        self.master = master

        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)

    def set_window_title(self, name=None):
        pass

    def new_file(self):
        pass

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension="txt", filetypes=[("All Files", "*.*"), 
        ("Text Files", "*.txt"), 
        ("Python Scripts", "*.py"), 
        ("Java Files", "*.java"),
        ("Markdown Documents", "*.md"), 
        ("JavaScript Files", "*.js"), 
        ("HTML Documents", "*.html"),
        ("CSS Documents", "*.css")]

        )
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())

    def save(self):
        pass

    def save_as(self):
        pass



if __name__ == "__main__":
    master = tk.Tk()
    pt = MillyText(master)
    master.mainloop()
