import random

names = ["Jenny", "Jerold", "Jean-Luc", "CJ", "Sarah", "Lee", "Chris"]


def whoBuysFood(names):
    return names[random.randint(0,len(names))]


def displayResult(name):
    print "Haha haha, " + whoBuysFood(names) + ", Python has decided that you are buying food for next week."

displayResult(whoBuysFood(names))