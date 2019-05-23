import pyglet

def makeChoice():
    choice = input()
    if isinstance(choice, int):
        return choice
    else:
        return 0