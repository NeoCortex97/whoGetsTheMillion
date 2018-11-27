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
        self.debug = False

    def append(self, q=Question()):
        self.questions.append(q)

    def parse(self, lines=[]):
        #print("\x1B[31msplitting lines\x1B[0m")
        #lines = text.split("\n")
        # print(lines[0][:7])
        # print("lines recived by pool" + str(lines))
        if len(lines) > 0:
            if lines[0][:7] == "P START":
                if self.debug:
                    print("\x1B[31mdetected start of pool\x1B[0m")
                    print("\x1B[31mparsing question #1\x1B[0m")
                self.difficulty = int(lines[0][8:])
                for i in range(1, len(lines), 6):
                    if self.debug:
                        print("\x1B[31m" + lines[i][:-1] + "\x1B[0m")
                    if len(lines[i]) > 0 and lines[i][0] == "Q":
                        #q = ""
                        #for j in range(6):
                        #    print("\x1B[31mappending: " + lines[i + j] + "\x1B[0m")
                        #    q += lines[i + j] + "\n"
                        self.questions.append(Question())
                        # print("\x1B[31mparsing question #" + str(len(self.questions) + 1) + "\x1B[0m")
                        self.questions[-1].parse(lines[i:i + 6])
                        if self.debug:
                            print(lines[i:i + 6])
                            self.questions[-1].dbgPrint()
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
