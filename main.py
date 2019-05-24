import pygame
import random


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
        if self.current_music == choice - 1:
            return 1
        else:
            return 0

    def make_choice(self, choice: int):
        if isinstance(choice, int):
            return self.check_choice(choice)
        else:
            self.print_error()
            return 0

    def play_music(self):
        print(self.music[self.current_music])
        pygame.mixer.init()
        pygame.mixer.music.load(self.music[self.current_music])
        pygame.mixer.music.play(0)

        clock = pygame.time.Clock()
        clock.tick(10)
        while pygame.mixer.music.get_busy():
            clock.tick(5)

    def print_error(self):
        return 'Invalid choice. Please, retype!'

    def get_variants(self):
        return self.variants


'''
1) print variants and play sound choice
2) make choice
3) print result
4) repeat

'''


def print_vars(variants: [str]):
    num = 1
    print('\n')
    for i in variants:
        print(str(num) + '. ' + i)
        num += 1


if __name__ == '__main__':
    pool = Pool()
    pool.add_music('music/lazzyTown.wav', 'Super Ice - We are number one')
    pool.add_music('music/BackInBlack.wav', 'AC/DC - Back In Black')
    pool.set_random_current_music()
    while True:
        print_vars(pool.get_variants())
        choice = input('Num/exit/play: ')
        if choice == 'exit':
            break
        elif choice == 'play':
            pool.play_music()
        else:
            result = pool.make_choice(int(choice))
            if result:
                print('You WIN!')
            else:
                print('You LOSE!')
            pool.set_random_current_music()
