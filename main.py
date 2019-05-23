import pygame
import random


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
        self.current_music = -1

    def add_variant(self, name: str):
        self.variants.append(name)

    def add_music(self, path: str, name: str):
        self.music.append(path)
        self.add_variant(name)

    def set_random_current_music(self):
        if len(self.music) > 0:
            self.current_music = random.randint(0, len(self.music) - 1)

    def check_choice(self, choice: int):
        if self.current_music == choice:
            print('You WIN!')
        else:
            print('You LOSE!')

    def play_music(self):
        print(self.music[self.current_music])
        pygame.mixer.init()
        sound = pygame.mixer.Sound(self.music[self.current_music])
        sound.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def print(self):
        for i in self.variants:
            print(i)


'''
1) print variants and play sound choice
2) make choice
3) print result
4) repeat

'''
if __name__ == '__main__':
    pool = Pool()
    pool.add_music('music/lazzyTown.wav', 'Super Ice - We are number one')
