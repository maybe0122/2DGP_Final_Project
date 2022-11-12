from pico2d import *

import game_framework
import count_state
import play_state

image = None
font = None

def enter():
    global image, font
    image = load_image('source/image/title_2.png')
    font = load_font('ENCR10B.TTF', 50)

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
                    game_framework.change_state(count_state)
                    # game_framework.change_state(play_state)
def draw():
    clear_canvas()
    image.draw(750 // 2, 900 // 2)
    font.draw(80, 110, 'Press Space to Start', (255, 0, 0))
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
