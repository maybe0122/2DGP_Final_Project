from pico2d import *
import play_state

class Background:
    def __init__(self):
        self.image = load_image('source/image/background1.png')
        self.font = load_font('source/font/ENCR10B.TTF', 30)

    def draw(self):
        self.image.draw(740 / 2, 900 / 2)
        self.font.draw(5, 900 - 10, f'Score : {play_state.player.score}', (255, 0, 0))

    def update(self):
        pass