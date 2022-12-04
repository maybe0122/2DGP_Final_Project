from pico2d import *
import game_framework
import play_state

image = None
font = None
title_font = None


def enter():
    global image, font, title_font, bgm
    image = load_image('source/image/title_2.png')
    font = load_font('source/font/ENCR10B.TTF', 50)
    title_font = load_font('source/font/ENCR10B.TTF', 70)


def exit():
    global image, font, title_font
    del image, font, title_font


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                game_framework.change_state(play_state)


def draw():
    clear_canvas()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    title_font.draw(50, 700, 'The Last Dragon', (255, 0, 0))
    font.draw(80, 110, 'Press Space to Start', (255, 0, 0))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
