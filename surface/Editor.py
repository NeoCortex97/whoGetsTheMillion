# -*- coding: utf-8 -*-
import tkinter as tk
from engine.Player import Player
from surface.qPanel import QuestionEditPanel


class EditorUi:
    def __init__(self):
        self.player = Player()
        self.oldText = ""

        self.editWindow = tk.Tk()
        self.editWindow.title = "Who Gets The Million - EDITOR"

        self.menuFrame = tk.Frame(self.editWindow)
        self.openButton = tk.Button(self.menuFrame, text="OPEN")
        self.saveButton = tk.Button(self.menuFrame, text="SAVE")
        self.newButton = tk.Button(self.menuFrame, text="NEW COLLECTION")

        self.poolFrame = tk.Frame(self.editWindow)
        self.currentPool = tk.StringVar(self.editWindow)
        self.currentPool.set("Create new")
        self.currentPool.trace("w", self.changedPool)
        self.poolDropdownList = list(self.player.getPools())
        self.poolDropdownList.append("Create new")
        self.poolOptions = tk.OptionMenu(self.poolFrame, self.currentPool, *self.poolDropdownList)
        self.questionList = tk.Listbox(self.poolFrame)
        self.newQuestionButton = tk.Button(self.poolFrame, text="New Question", command=self.appenQuestion)
        self.editQuestionButton = tk.Button(self.poolFrame, text="EDIT", command=self.loadQuestion)

        self.editPanel = QuestionEditPanel(self.editWindow, "OK", "50/50")

        # self.questionFrame = tk.Frame(self.editWindow)
        # self.currentText = tk.StringVar()
        # self.textLabel = tk.Label(self.questionFrame, text="Text:")
        # self.textField = tk.Entry(self.questionFrame, textvariable=self.currentText)

        # self.currentAText = tk.StringVar()
        # self.answerALabel = tk.Label(self.questionFrame, text="A:")
        # self.answerAField = tk.Entry(self.questionFrame, textvariable=self.currentAText)
        # self.answerACorrect = tk.Checkbutton(self.questionFrame, text=corr)
        # self.answerAFifty = tk.Checkbutton(self.questionFrame, text=ff)
        #
        # self.currentBText = tk.StringVar()
        # self.answerBLabel = tk.Label(self.questionFrame, text="B:")
        # self.answerBField = tk.Entry(self.questionFrame, textvariable=self.currentBText)
        # self.answerBCorrect = tk.Checkbutton(self.questionFrame, text=corr)
        # self.answerBFifty = tk.Checkbutton(self.questionFrame, text=ff)
        #
        # self.currentCText = tk.StringVar()
        # self.answerCLabel = tk.Label(self.questionFrame, text="C:")
        # self.answerCField = tk.Entry(self.questionFrame, textvariable=self.currentCText)
        # self.answerCCorrect = tk.Checkbutton(self.questionFrame, text=corr)
        # self.answerCFifty = tk.Checkbutton(self.questionFrame, text=ff)
        #
        # self.currentDText = tk.StringVar()
        # self.answerDLabel = tk.Label(self.questionFrame, text="D:")
        # self.answerDField = tk.Entry(self.questionFrame, textvariable=self.currentDText)
        # self.answerDCorrect = tk.Checkbutton(self.questionFrame, text=corr)
        # self.answerDFifty = tk.Checkbutton(self.questionFrame, text=ff)
        #
        # self.buttonFrame = tk.Frame(self.questionFrame)
        # self.applyButton = tk.Button(self.buttonFrame, text="APPLY", command=self.applyQuestion)
        # self.deleteButton = tk.Button(self.buttonFrame, text="DELETE")

        # Setup window
        self.newButton.pack(side=tk.LEFT)
        self.openButton.pack(side=tk.LEFT)
        self.saveButton.pack(side=tk.LEFT)
        self.menuFrame.pack(side=tk.TOP, anchor=tk.W)

        self.poolOptions.pack(side=tk.TOP, fill=tk.X)
        self.questionList.pack(side=tk.TOP, fill=tk.X)
        self.newQuestionButton.pack(side=tk.LEFT, anchor=tk.SW, fill=tk.X)
        self.editQuestionButton.pack(side=tk.RIGHT, anchor=tk.SE, fill=tk.X)
        self.poolFrame.pack(side=tk.LEFT)

        # self.textLabel.grid(row=0)
        # self.answerALabel.grid(row=1)
        # self.answerBLabel.grid(row=2)
        # self.answerCLabel.grid(row=3)
        # self.answerDLabel.grid(row=4)
        # # self.textField.grid(row=0, column=1)
        # self.answerAField.grid(row=1, column=1)
        # self.answerBField.grid(row=2, column=1)
        # self.answerCField.grid(row=3, column=1)
        # self.answerDField.grid(row=4, column=1)
        # self.answerACorrect.grid(row=1, column=2)
        # self.answerBCorrect.grid(row=2, column=2)
        # self.answerCCorrect.grid(row=3, column=2)
        # self.answerDCorrect.grid(row=4, column=2)
        # self.answerAFifty.grid(row=1, column=3)
        # self.answerBFifty.grid(row=2, column=3)
        # self.answerCFifty.grid(row=3, column=3)
        # self.answerDFifty.grid(row=4, column=3)
        #
        # self.applyButton.pack(side=tk.LEFT, anchor=tk.W, fill=tk.X)
        # self.deleteButton.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.X)
        # self.buttonFrame.grid(row=5, columnspan=4)
        #
        # self.questionFrame.pack(side=tk.RIGHT, anchor=tk.NW)

        # start looping
        self.editWindow.mainloop()

    def loadQuestionList(self, difficultie=0):
        self.questionList.delete(0, tk.END)
        questions = self.player.collection.getQuestions(difficultie)
        for i, e in enumerate(questions):
            self.questionList.insert(i, e["text"])

    def changedPool(self, *args):
        print(self.currentPool.get())
        if self.currentPool.get() == "Create new":
            self.poolDropdownList.append(str(len(self.poolDropdownList) - 1))
            self.currentPool.set(str(len(self.poolDropdownList) - 2))
            self.updateDropdown()
        else:
            pass
            # self.loadQuestionList(int(self.currentPool.get()))

    def updateDropdown(self):
        menu = self.poolOptions["menu"]
        menu.delete(0, tk.END)
        # print(self.poolDropdownList)
        for i in self.poolDropdownList:
            # print("Set {}".format(i))
            menu.add_command(label=str(i), command=lambda value=str(i): self.currentPool.set(value))

    def appenQuestion(self):
        self.player.collection.append(int(self.currentPool.get()), "New question")
        self.loadQuestionList(int(self.currentPool.get()))

    def loadQuestion(self):
        q = self.player.collection.getQuestionByText(int(self.currentPool.get()), self.questionList.get(self.questionList.curselection()))
        # print("q = {}".format(q))
        self.oldText = q["text"]
        self.currentText.set(q["text"])
        self.currentAText.set(q["a"])
        self.currentBText.set(q["b"])
        self.currentCText.set(q["c"])
        self.currentDText.set(q["d"])



    def applyQuestion(self):
        self.player.collection.editQuestionByText(self.oldText, self.currentText.get(), self.currentAText.get(), self.currentBText.get(), self.currentCText.get(), self.currentDText.get(), self.mkCorrect(), self.mkFiftyFifty())

    def mkCorrect(self):
        pass

    def mkFiftyFifty(self):
        pass


if __name__ == '__main__':
    e = EditorUi()
