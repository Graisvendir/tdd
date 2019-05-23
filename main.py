import pyglet

def makeChoice():
    choice = input()
    if isinstance(choice, int):
        return choice
    else:
        return 0

class Pool:

    def __init__(self):
        self.pool = []

    def print(self):
        print()