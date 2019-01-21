# -*- coding: utf-8 -*-
import tkinter as tk


class AnswerFrame(tk.Frame):
    def __init__(self, parent=None, label="A", correct="OK", ff="50/50"):
        tk.Frame.__init__(self, parent)
        self.text = tk.StringVar()
        self.labelLabel = tk.Label(self, text=label)
        self. textEntry = tk.Entry(self, textvariable=self.text)

        self.correct = tk.IntVar()
        self.corrBox = tk.Checkbutton(self, text=correct)

        self.fiftyfifty = tk.IntVar()
        self.fiftyfiftyBox = tk.Checkbutton(self, text=ff)
        self.packContent()

    def setText(self, value=str()):
        self.text.set(value)

    def getText(self):
        self.text.get()

    def packContent(self):
        self.labelLabel.grid(row=0)
        self.textEntry.grid(row=0, column=1)
        self.corrBox.grid(row=0, column=2)
        self.fiftyfiftyBox.grid(row=0, column=3)


if __name__ == '__main__':
    w = tk.Tk()
    a = AnswerFrame(w)
    # a.packContent()
    a.pack()
    w.mainloop()
