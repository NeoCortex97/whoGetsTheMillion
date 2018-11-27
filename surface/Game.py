import tkinter as tk
from engine.Player import Player


class GameUi:
    def __init__(self):
        self.player = Player()

        self.gameWindow = tk.Tk()
        self.jokerFrame = tk.Frame(self.gameWindow)
        self.halfJoker = tk.Button(self.jokerFrame, text="50/50")
        self.audienceJoker = tk.Button(self.jokerFrame, text="Publikum")
        self.startBtn = tk.Button(self.gameWindow, text="START", bg="gray", command=self.start)
        self.question = tk.Label(self.gameWindow)
        self.score = tk.Label(self.gameWindow, text=self.player.getLevel())
        self.answerA = tk.Button(self.gameWindow, bg="blue")
        self.answerB = tk.Button(self.gameWindow, bg="blue")
        self.answerC = tk.Button(self.gameWindow, bg="blue")
        self.answerD = tk.Button(self.gameWindow, bg="blue")

        self.halfJoker.pack(side=tk.RIGHT)
        self.audienceJoker.pack(side=tk.RIGHT)

        self.gameWindow.title("Wer wird Millionär ?")
        self.gameWindow.geometry("500x500")

        self.startBtn.pack(fill=tk.X, side=tk.TOP)
        self.jokerFrame.pack(side=tk.TOP)
        self.score.pack(fill=tk.X, side=tk.TOP)
        self.answerD.pack(fill=tk.X, side=tk.BOTTOM)
        self.answerC.pack(fill=tk.X, side=tk.BOTTOM)
        self.answerB.pack(fill=tk.X, side=tk.BOTTOM)
        self.answerA.pack(fill=tk.X, side=tk.BOTTOM)
        self.question.pack(fill=tk.X, side=tk.BOTTOM)
        self.gameWindow.mainloop()

    def start(self):
        print("\x1B[41mstart\x1B[0m")
        q = self.player.getQuestion()
        # print("Question: " + q["text"])
        # print("A: " + q["a"]["text"])
        # print("B: " + q["b"]["text"])
        # print("C: " + q["c"]["text"])
        # print("D: " + q["d"]["text"])
        self.question.config(text=q["text"])
        self.answerA.config(text=q["a"]["text"])
        self.answerB.config(text=q["b"]["text"])
        self.answerC.config(text=q["c"]["text"])
        self.answerD.config(text=q["d"]["text"])
        self.score.config(text=self.player.getLevel())