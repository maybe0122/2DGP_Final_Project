import pico2d
from pico2d import *
import title_state
import menu_state
import random
import game_framework

class Dragon:
    def __init__(self):
        self.x, self.y = random.randint(100, 700),100
        self.frame = 0
        self.image = load_image('source/image/flying_dragon-red.png')

    def update(self):
        self.frame = (self.frame + 1) % 3
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 144, 128 * 3, 144, 128, self.x, self.y)
        pass


class Field:
    # def __init__(self):
    #     self.image = load_image('')
    pass

class Enemy:
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.type == SDLK_ESCAPE:   # press esc to move menu
                game_framework.change_state(menu_state)
            elif event.type == SDLK_w:  # up
                pass
            elif event.type == SDLK_a:  # left
                pass
            elif event.type == SDLK_s:  # down
                pass
            elif event.type == SDLK_d:  # right
                pass
        elif event.type == SDL_KEYUP:
            if event.type == SDLK_w:    # up
                pass
            elif event.type == SDLK_a:  # left
                pass
            elif event.type == SDLK_s:  # down
                pass
            elif event.type == SDLK_d:  # right
                pass

def test_self():
    import sys
    pico2d.open_canvas(800, 950)
    game_framework.run(sys.modules['__main__'])
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()


open_canvas(800, 950)
dragon = Dragon()

running = True

while running:
    handle_events()
    dragon.update()

    clear_canvas()
    dragon.draw()
    update_canvas()
    delay(0.15)

close_canvas()