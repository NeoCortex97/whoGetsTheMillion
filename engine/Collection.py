from engine.Pool import Pool
from engine.Loader import Loader

class Collection:
    def __init__(self, path = ""):
        self.pools = []
        self.debug = False
        if path != "":
            self.load(path)

    def append(self, p=Pool()):
        self.pools.append(p)

    def parse(self, lines=[]):
        start = 0
        if self.debug:
            print("Lines passed to Collection: ", lines)
            print("Collection parses: ")
        for i in range(len(lines)):
            # print(lines[i][:5])
            if self.debug:
                print("Testing line: ", lines[i])
            if lines[i][:7] == "P START":
                start = i
                if self.debug:
                    print("start of pool is: " + str(i))
            if lines[i][:5] == "P END":
                if self.debug:
                    print("parsing new pool")
                self.pools.append(Pool())
                p = lines[start:i]
                if self.debug:
                    print(p)
                self.pools[-1].parse(lines[start:i])
                p.clear()
                if self.debug:
                    print("lines passed to pool" + str(lines[start:i]))
                    self.pools[-1].dbgPrint()
        if self.debug:
            self.dbgPrint()

    def toString(self):
        res = ""
        for p in self.pools:
            res += p.toString() + "\n"
        return res

    def dbgPrint(self):
        for p in self.pools:
            p.dbgPrint()


    def load(self, path):
        l = Loader(path)
        l.load()
        l.prepare()
        self.parse(l.getLines())

    def getQuestionFromPool(self, level=0):
        for p in self.pools:
            if level == p.getLevel():
                if self.debug:
                    print("Pool level is: " + str(p.getLevel()))
                question = p.getRandom()
                # print("The collection object thinks the question is:")
                # question.dbgPrint(.an)
                return question
