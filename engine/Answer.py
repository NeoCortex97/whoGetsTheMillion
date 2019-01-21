"""
    <CF> "<TEXT>"
    TEXT => Text of the answer
    CF   => correct or fifty/fifty
                 C | F
            -------|----
            0 -> f | f
            1 -> t | t
            2 -> f | t
            3 -> t | f
    Example:
        "How are you?"
        1 "fine"
        0 "miserable"
        2 "okay"
        3 "good"
"""

class Answer:
    def __init__(self, text="", correct=False, fty2=False, percent=0):
        self.text = text
        self.correct = correct
        self.fiftyFifty = fty2
        self.percentage = 0
        self.debug = False

    def fill(self, text="", correct=False, fty2=False, percent=0):
        self.text = text
        self.correct = correct
        self.fiftyFifty = fty2
        self.percentage = percent

    def parse(self, text):
        if self.debug:
            print("\x1B[33mAntwort Text ist:" + text[:-1] + "\x1B[0m")
        if (text[0] in "0123") and text[1] == " ":
            self.decodeNumber(int(text[0]))
            if text[2] == "\"" and text[-1] == "\"":
                if self.debug:
                    print("Set answer text to: " + text[3:-1])
                self.text = text[3:-1]
            else:
                if text[2] == "\"":
                    if self.debug:
                        print("first quote detected")
                if text[-1] == "\"":
                    if self.debug:
                        print("second quote detected")
                print("falscher string")
                # TODO: create exeption for incorrect formatted answer strings
                # Exeption stuff
                pass
        else:
            if self.debug:
                print("falsche zahl")
            # TODO: create exeption for incorrect encoding of correctness and fifty fifty joker
            # Exeption stuff
            pass
        if self.debug:
            print("This is in answer:")
            self.dbugPrint()
        return self

    def decodeNumber(self, num=0):
        if self.debug:
            print("\x1B[33mencoded number is: " + str(num) + "\x1B[0m")
        if num == 0:
            self.correct = False
            self.fiftyFifty = False
        elif num == 1:
            self.correct = True
            self.fiftyFifty = True
        elif num == 2:
            self.correct = False
            self.fiftyFifty = True
        elif num == 3:
            self.correct = True
            self.fiftyFifty = False

    def encodeNumber(self):
        if not self.correct and not self.fiftyFifty:
            return 0
        elif self.correct and self.fiftyFifty:
            return 1
        elif not self.correct and self.fiftyFifty:
            return 2
        else:
            return 3

    def dbugPrint(self):
        print("{0:<6} | {1:<6} | {2:>3}% | {3}".format(str(self.correct),
                                                       str(self.fiftyFifty),
                                                       self.percentage,
                                                       self.text))

    def toString(self):
        return "{0} \"{1}\"".format(self.encodeNumber(), self.text)