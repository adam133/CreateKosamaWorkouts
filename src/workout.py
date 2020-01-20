import tkinter as tk
from tkinter import filedialog
import json


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.openfile = tk.Button(self)
        self.openfile["text"] = "Select workout file"
        self.openfile["command"] = self.open_file
        self.openfile.pack(side="top")

        self.quit = tk.Button(self,
                              text="QUIT",
                              fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def file_opened(self):
        with open(self.filename) as json_config_file:
            workout = json.load(json_config_file)



    def open_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select file",
                                                   filetypes=(("text files", "*.txt"),
                                                              ("all files", "*.*")))
        print(self.filename)
        self.file_opened()



root = tk.Tk()
app = Application(master=root)
app.mainloop()
