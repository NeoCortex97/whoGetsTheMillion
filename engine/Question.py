from engine.Answer import Answer

"""
    Q "<TEXT>"
    T <TAG> <TAG> <TAG> ...
    A <CF> "<TEXT>"
    B <CF> "<TEXT>"
    C <CF> "<TEXT>"
    D <CF> "<TEXT>"
"""


class Question:
    def __init__(self, text="", a=Answer(), b=Answer(), c=Answer(), d=Answer(), tags=""):
        self.text = text
        self.answers = [a, b, c, d]
        self.tags = tags.split()
        self.debug = False

    def fillAnswer(self, pos="", text="", correct=False, fty2=False, percent=0):
        index = 0
        if pos == "a":   index = 0
        elif pos == "b": index = 1
        elif pos == "c": index = 2
        elif pos == "d": index = 3
        self.answers[index] = Answer(text, correct, fty2, percent)

    def parseAnswer(self, pos="", text=""):
        index = 0
        if pos.lower() == "a":   index = 0
        elif pos.lower() == "b": index = 1
        elif pos.lower() == "c": index = 2
        elif pos.lower() == "d": index = 3
        self.answers[index].parse(text)
        # self.answers[index].dbugPrint()

    def setText(self, text):
        self.text = text

    def setTags(self, tags):
        self.tags = tags.split()

    def parse(self, lines=[]):
        # if text[-1] == "\n":
        #    text = text[:-1]
        #    print("\x1B[32mremoved last newline\x1B[0m")
        #lines = text.split("\n")
        if self.debug:
            print("The strings passed to parse", lines)
        for line in lines:
            if self.debug:
                print("\x1B[32mprocessing line: " + line[:-1] + "\x1B[0m")
            if line[0] == "Q":
                if self.debug:
                    print("\x1B[32mdetected question line\x1B[0m")
                if (line[2] == "\"") and (line[-1 == "\""]):
                    self.text = line[3:-2]
                    if self.debug:
                        print("\x1B[32mset text to: " + line[3:-1] + "\x1B[0m")
                else:
                    if self.debug:
                        print("fehlende anführungszeichen")
                    # TODO: Create exeption for missing ticks
                    # Exeption Stuff
                    pass
            elif line[0] == "T":
                if self.debug:
                    print("\x1B[32mdetected tag line\x1B[0m")
                self.tags = line[2:].split()
            elif line[0] in "ABCD":
                if self.debug:
                    print("\x1B[32mdetected anwer line\x1B[0m")
                self.parseAnswer(line[0], line[2:])
            else:
                if self.debug:
                    print("falsche zeile")
                # TODO: Create exeption for incorrect line
                # Exeption stuff
                pass
        if self.debug:
            print("This is in Question:")
            self.dbgPrint()

    def toString(self):
        qline = "Q \"{0}\"".format(self.text)
        taglist = ""
        for t in self.tags:
            taglist += " " + t
        tline = "T{}\n".format(taglist)
        aline = "A {}\n".format(self.answers[0].toString())
        bline = "B {}\n".format(self.answers[1].toString())
        cline = "C {}\n".format(self.answers[2].toString())
        dline = "D {}\n".format(self.answers[3].toString())
        return "{0}{1}{2}{3}{4}{5}\n".format(qline, tline, aline, bline, cline, dline)

    def dbgPrint(self):
        print("Frage: " + self.text)
        for a in self.answers:
            a.dbugPrint()

    def getText(self):
        return self.text

    def getAnswer(self, name=""):
        index = 0
        if name.lower() == "a":
            index = 0
        elif name.lower() == "b":
            index = 1
        elif name.lower() == "c":
            index = 2
        elif name.lower() == "d":
            index = 3
        return self.answers[index].text

    def getQuestion(self):
        if self.debug:
            print("Question.getQuestion:")
            self.dbgPrint()
        return {"text": self.getText(),
                "a": {"correct": self.answers[0].correct, "text": self.answers[0].text},
                "b": {"correct": self.answers[1].correct, "text": self.answers[1].text},
                "c": {"correct": self.answers[2].correct, "text": self.answers[2].text},
                "d": {"correct": self.answers[3].correct, "text": self.answers[3].text}}
