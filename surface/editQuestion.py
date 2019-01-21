# -*- coding: utf-8 -*-
import tkinter as tk


class QuestionEditFrame(tk.Frame):
    def __init__(self, parent=None, labelText="Question", text=""):
        tk.Frame.__init__(self, parent)
        self.text = tk.StringVar()
        self.label = tk.Label(self, text=labelText)
        self.qEdit = tk.Entry(self, textvariable=self.text)
        self.setupContent()

    def get(self):
        return self.qEdit.get()

    def setupContent(self):
        self.label.grid(row=0)
        self.qEdit.grid(row=0, column=1)


if __name__ == '__main__':
    w = tk.Tk()
    q = QuestionFrame(w)
    q.pack()
    w.mainloop()
