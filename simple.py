# -*- coding: utf-8 -*-
import json
import random
import sys


def load(path):
    with open(path, "r") as f:
        data = json.load(f)
        return data


def main(**kwargs):
    if len(sys.argv) < 2:
        print("FEHLER: Keine Daten gefunden.\nEs muss eine json Datei mit fragen angegeben werden!")
        print("Beispiel: python3 simple.py test.json")
    else:
        fragen = load(sys.argv[1])
        running = True
        while running:
            aktuell = random.choice(fragen["fragen"])
            print("Frage: {}\nA: {}\nB: {}\nC: {}\nD: {}".format(aktuell["text"], aktuell["a"], aktuell["b"], aktuell["c"], aktuell["d"]))
            choice = " "
            while choice.lower() not in "abcd":
                choice = input("Antwort: ")
            if choice in aktuell["richtig"]:
                print("Diese Antwort ist richtig!")
            else:
                print("Die richtige Antwort(en) wäre(n) {}".format(aktuell["richtig"]))
            weiter = input("Weiter? (Yn)")
            if weiter.lower() == "n":
                running = False


if __name__ == "__main__":
    main()
