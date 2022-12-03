import game_framework
from pico2d import *
import save_score_state
import background

image = None
font = None
logo_time = 0.0

def enter():
    global image, font
    image = load_image('source/image/background1.png')
    font = load_font('source/font/ENCR10B.TTF', 100)

def exit():
    global image
    del image

def update():
    global logo_time
    if logo_time > 0.5:
        logo_time = 0
        game_framework.change_state(save_score_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    font.draw(get_canvas_width() // 2 - 260, get_canvas_height() // 2, 'GAME OVER', (255, 0, 0))
    update_canvas()

def handle_events():
    events = get_events()
