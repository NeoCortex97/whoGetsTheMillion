class Loader:
    def __init__(self, path=""):
        self.path = path
        self.lines = []
        self.debug = False

    def setPath(self, path=""):
        self.path = path

    def load(self):
        f = open(self.path, "r")
        self.lines = f.readlines()
        f.close()

    def prepare(self):
        #self.lines.remove("\n")
        self.lines = list(filter(lambda a: a != "\n", self.lines))
        for line in self.lines:
            if line[0] == "#":
                self.lines.remove(line)
                if self.debug:
                    print("removed comment line: " + line)
            if line[-1] == "\n":
                self.lines[self.lines.index(line)] = line[:-1]
                if self.debug:
                    print("removed newline")
            if len(line) == 0:
                self.lines.remove(line)
                if self.debug:
                    print("removed empty line")

    def getLines(self):
        return self.lines
