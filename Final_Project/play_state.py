import pico2d
from pico2d import *
import title_state
import menu_state
import random
import game_framework
import count_state

class Dragon:
    def __init__(self):
        self.x, self.y = 800 // 2, 64
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.image = load_image('source/image/flying_dragon-red.png')

    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
        self.x = clamp(0 + 72, self.x, 800 - 72)
        self.y = clamp(0 + 54, self.y, 950 - 54)


    def draw(self):
        self.image.clip_draw(self.frame * 144, 128 * 3, 144, 128, self.x, self.y)

class Field:
    # def __init__(self):
    #     self.image = load_image('')
    pass

class Enemy:
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:   # press esc to move menu
                game_framework.push_state(menu_state)
            elif event.key == SDLK_w:  # up
                dragon.dir_y += 1
            elif event.key == SDLK_a:  # left
                dragon.dir_x -= 1
            elif event.key == SDLK_s:  # down
                dragon.dir_y -= 1
            elif event.key == SDLK_d:  # right
                dragon.dir_x += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:    # up
                dragon.dir_y -= 1
            elif event.key == SDLK_a:  # left
                dragon.dir_x += 1
            elif event.key == SDLK_s:  # down
                dragon.dir_y += 1
            elif event.key == SDLK_d:  # right
                dragon.dir_x -= 1

running = True
dragon = None

def test_self():
    import sys
    pico2d.open_canvas(800, 950)
    game_framework.run(sys.modules['__main__'])
    pico2d.clear_canvas()

def enter():
    global running, dragon
    dragon = Dragon()
    running = True

def exit():
    global dragon
    del dragon

def update():
    dragon.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    dragon.draw()

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    test_self()