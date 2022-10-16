import game_framework
from pico2d import *
import play_state
import menu_state

image = None
frame = 0
count = 3

def enter():
    global image
    image = load_image('source/image/count.png')

def exit():
    global image
    del image

def update():
    global count
    if count < 0:
        count = 3
        if menu_state.new == True:
            game_framework.change_state(play_state)
        else:
            game_framework.push_state(play_state)
    count -= 1

def draw():
    global frame
    clear_canvas()
    image.clip_draw(frame * 134, 0, 134, 255, 400, 950 // 2)
    frame += 1
    if frame > 1:
        delay(1)
    update_canvas()

def handle_events():
    events = get_events()

def pause():
    pass

def resume():
    pass