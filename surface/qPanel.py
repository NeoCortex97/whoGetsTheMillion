# -*- coding: utf-8 -*-
import tkinter as tk
from surface.editQuestion import QuestionEditFrame
from surface.editAnswer import AnswerFrame


class QuestionEditPanel (tk.Frame):
    def __init__(self, parent=None, corr="", ff=""):
        tk.Frame.__init__(self, parent)
        self.question = QuestionEditFrame(parent)
        self.question.pack()
        self.A = AnswerFrame(parent, correct=corr, ff=ff)
        self.B = AnswerFrame(parent, "B", corr, ff)
        self.C = AnswerFrame(parent, "C", corr, ff)
        self.D = AnswerFrame(parent, "D", corr, ff)
        self.A.pack()
        self.B.pack()
        self.C.pack()
        self.D.pack()

class QuestionDisplayPanel (tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.A = tk.Button(parent, bg="blue")
        self.B = tk.Button(parent, bg="blue")
        self.C = tk.Button(parent, bg="blue")
        self.D = tk.Button(parent, bg="blue")