from pico2d import *
import game_framework
import game_world

from dragon import Dragon

import title_state
import menu_state
import random

import count_state
import dragon

dragon = None
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(menu_state) # press esc to move menu
        else:
            dragon.handle_events(event)


def enter():
    global dragon
    dragon = Dragon()
    game_world.add_object(dragon, 0)

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_object():
        game_object.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    for game_object in game_world.all_object():
        game_object.draw()

def pause():
    pass

def resume():
    pass

def test_self():
    import play_state

    pico2d.open_canvas(800, 950)
    game_framework.run(play_state)
    pico2d.clear_canvas()


if __name__ == '__main__':
    test_self()
