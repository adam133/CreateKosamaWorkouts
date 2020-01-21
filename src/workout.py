import tkinter as tk
from tkinter import filedialog
from tkinter import *
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
                              text="Quit",
                              fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def next_item(self):
        self.current_item = self.workout.pop(0)
        self.workout_text.set(self.current_item["text"])
        self.timer_text.set(int(self.current_item["time"]))

    def update_workout(self):
        timer = int(self.timer_text.get())
        self.timer_text.set(timer - 1)
        if timer <= 0:
            self.next_item()
        elif len(self.workout) == 0:
            self.workout_text.set("Workout Complete! Nice Job!")
            self.after(5000, self.master.destroy)

        self.after(1000, self.update_workout)

    def start_workout(self):
        w = self.workout["workout"]
        self.current_item = w.pop(0)
        self.workout = w

        self.workout_text = StringVar()
        self.workout_text_label = tk.Label(self,
                                           textvariable=self.workout_text,
                                           fg="black",
                                           font=("Times", 20, "bold")).pack()
        self.workout_text.set(self.current_item["text"])

        self.timer_text = StringVar()
        self.workout_timer_label = tk.Label(self,
                                            textvariable=self.timer_text,
                                            fg="red",
                                            font=("Times", 30, "bold")).pack(side="bottom")
        self.timer_text.set(int(self.current_item["time"]))
        self.after(1000, self.update_workout)

        self.next_item_butt = tk.Button(self,
                              text="Skip this item",
                              fg="green",
                              command=self.next_item)
        self.next_item_butt.pack(side="right")

    def file_opened(self):
        with open(self.filename) as json_config_file:
            self.workout = json.load(json_config_file)

        self.openfile.destroy()
        self.quit.pack(side="top")
        print(self.workout)
        self.start_workout()

    def open_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select file",
                                                   filetypes=(("text files", "*.txt"),
                                                              ("all files", "*.*")))
        print(self.filename)
        self.file_opened()


root = tk.Tk()
root.title = "Workout"
root.geometry("600x600")
app = Application(master=root)
app.title = "Workout"
app.mainloop()
