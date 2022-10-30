import pico2d
from pico2d import *
import title_state
import menu_state
import random
import game_framework
import count_state
import dragon

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(menu_state) # press esc to move menu
        else:
            dragon.handle_events(event)

running = True
dragon = None

def test_self():
    import sys
    pico2d.open_canvas(800, 950)
    game_framework.run(sys.modules['__main__'])
    pico2d.clear_canvas()

def enter():
    global running, dragon
    dragon = dragon.Dragon()
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