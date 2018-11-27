from engine.Collection import Collection
from engine.Question import Question


class Player:
    def __init__(self, name="", path="test.txt"):
        self.name = name
        self.level = 0
        self.collection = Collection(path)
        self.fiftyFiftyJoker = True
        self.publikumJoker = True

    def getLevel(self):
        return str(self.level) + "€"

    def getQuestion(self):
        question = self.collection.getQuestionFromPool(self.level)
        # print("Player object thinks the question is:")
        # question.dbgPrint()
        return question
