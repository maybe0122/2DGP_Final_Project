from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('source/image/background1.png')
        self.score = 0
        self.font = load_font('ENCR10B.TTF', 30)

    def draw(self):
        self.image.draw(740 / 2, 900 / 2)
        self.font.draw(5, 900 - 10, f'Score : {self.score}', (255, 0, 0))

    def update(self):
        pass