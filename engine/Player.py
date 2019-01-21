from engine.jsonCollection import Collection
from engine.Question import Question


class Player:
    def __init__(self, name="", path="test.json"):
        self.name = name
        self.level = 0
        self.collection = Collection(path)
        self.fiftyFiftyJoker = True
        self.publikumJoker = True

    def getLevel(self):
        return str(self.collection.getMoney(self.level)) + "€"

    def getQuestion(self):
        question = self.collection.random(self.level)
        # print("Player object thinks the question is:")
        # question.dbgPrint()
        return question

    def getPools(self):
        return self.collection.getPoolList()
