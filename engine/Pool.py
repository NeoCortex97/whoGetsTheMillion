from engine.Question import Question
from random import choice
"""
    P START <DIFFICULTY>
    Q "<TEXT>"
    T <TAG> <TAG> <TAG> ...
    A <CF> "<TEXT>"
    B <CF> "<TEXT>"
    C <CF> "<TEXT>"
    D <CF> "<TEXT>"
    
    Q "<TEXT>"
    ...
    P END
"""


class Pool:
    def __init__(self, diff=0):
        self.questions = []
        self.difficulty = diff
        self.debug = True

    def append(self, q=Question()):
        self.questions.append(q)

    def parse(self, lines=[]):
        if len(lines) > 0:
            if lines[0][:7] == "P START":
                if self.debug:
                    print("\x1B[31mdetected start of pool\x1B[0m")
                    print("\x1B[31mparsing question #1\x1B[0m")
                self.difficulty = int(lines[0][8:])
                for i in range(1, len(lines), 6):
                    if self.debug:
                        print("\x1B[31m" + lines[i][:-1] + "\x1B[0m")
                    if lines[i][0] == "Q":
                        self.questions.append(Question())
                        if self.debug:
                            print("\x1B[35mlisting all questions:")
                            self.dbgPrint()
                            print("\x1B[31mparsing question #" + str(len(self.questions) + 1) + "\x1B[0m")
                        end = i + 6
                        q = lines[i:end]
                        self.questions[-1].parse(q)
                        if self.debug:
                            print("\x1B[31m" + str(lines[i:i + 6]))
                            self.questions[-1].dbgPrint()
                            print("\x1B[35mlist all questions:")
                            self.dbgPrint()
                            print("\x1B[0m")
                    else:
                        # TODO: Create exeption for invalid entry length
                        # Exeption stuff
                        pass
            else:
                # TODO: Create exeption for invalid pool.
                # Exeption stuff
                pass
        else:
            # TODO: Exeption for empty list
            # Exeption stuff
            pass

    def toString(self):
        start = "P START {}\n\n".format(self.difficulty)
        questionlist = ""
        for q in self.questions:
            questionlist += q.toString()
        return "{0}{1}P END\n".format(start, questionlist)

    def dbgPrint(self):
        print("Difficulty: " + str(self.difficulty))
        for q in self.questions:
            q.dbgPrint()

    def getLevel(self):
        return self.difficulty

    def getRandom(self):
        question = choice(self.questions)
        # print("The Pool object thinks the question is:")
        # print(question)
        # question.dbgPrint()
        return question.getQuestion()
