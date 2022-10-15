from pico2d import *

import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('source/image/title_2.png')  #add title image

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.quit()
                elif event.key == SDLK_SPACE:
                    game_framework.change_state(play_state)
def draw():
    clear_canvas()
    image.draw(800 // 2, 950 // 2)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
