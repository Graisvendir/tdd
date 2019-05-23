import pyglet


def makeChoice():
    choice = input()
    if isinstance(choice, int):
        return choice
    else:
        return 0


class Pool:

    def __init__(self):
        self.variants = []
        self.music = []
        self.current_music = 0

    def add_variant(self, name: str):
        self.variants.append(name)

    def add_music(self, path: str):
        self.music.append(path)

    def print(self):
        for i in self.variants:
            print(i)


'''
1) print variants and play sound choice
2) make choice
3) print result
4) repeat

'''
