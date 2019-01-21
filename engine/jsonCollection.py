# -*- coding: utf-8 -*-
import json
import random


class Collection:
    def __init__(self, path=""):
        self.difficulties = dict()
        self.pools = dict()

        if path == "":
            self.difficulties = {0: 50, 1: 100, 2: 200, 3: 300, 4: 500, 5: 1000, 6: 2000, 7: 4000, 8: 8000, 9: 16000,
                                 10: 32000, 11: 64000, 12: 125000, 13: 500000, 14: 1000000}
            # self.pools = {0: [{"text": "", "a": "", "b": "", "c": "", "d": "", "correct": "", "fiftyfifty": ""}],
            #               1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: []}
        else:
            self.load(path)

    def load(self, file):
        try:
            with open(file, "r") as f:
                data = json.load(f)
                self.difficulties = data["difficulties"]
                self.pools = data["pools"]
        except FileNotFoundError:
            print("File not found")

    def random(self, difficulty=0):
        return random.choice(self.pools[difficulty])

    def getMoneyValues(self):
        return self.difficulties.values()

    def getDifficulties(self):
        return self.difficulties.keys()

    def save(self, path=""):
        with open(path, "w")as out:
            json.dump(self.__dict__, out, indent=4, sort_keys=True)

    def append(self, difficulty=0, text="", a="", b="", c="", d="", correct="", fiftyfifty=""):
        try:
            self.pools[difficulty].append({"text": text[:], "a": a[:], "b": b[:], "c": c[:], "d": d[:], "correct": correct[:], "fiftyfifty": fiftyfifty[:]})
        except KeyError:
            self.pools[difficulty] = [{"text": text[:], "a": a[:], "b": b[:], "c": c[:], "d": d[:], "correct": correct[:], "fiftyfifty": fiftyfifty[:]}]

    def getMoney(self, difficultie=0):
        return self.difficulties[difficultie]

    def getQuestions(self, difficultie=0):
        return self.pools[difficultie]

    def getPoolList(self):
        return self.pools.keys()

    def getQuestionByText(self, difficultie=0, text=""):
        # print("Text: {}".format(text))
        for e in self.pools[difficultie]:
            if e["text"] == text:
                return e
        else:
            print("did not find question")

    def editQuestionByText(self, textKey="", newText="", a="", b="", c="", d="", correct="", ff=""):
        pass

    def getRandomQuestion(self, level):
        return random.choice(self.pools["pools"][level])
