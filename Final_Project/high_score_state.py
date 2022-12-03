from pico2d import *
import game_framework
import title_state
import save_score_state

font = None
image = None
score = None
name = None
data = []
sorted_data = []
menu_image = None


def enter():
    global font, image, data, sorted_data, menu_image
    font = load_font('source/font/ENCR10B.TTF', 50)
    image = load_image('source/image/background1.png')
    menu_image = load_image('source/image/menu.png')
    data.append(save_score_state.load())
    sorted_data = sorted(data, key=lambda d: d['score'], reverse=True)


def exit():
    global font, image, menu_image
    del font, image, menu_image


def update():
    pass


def draw():
    global image, menu_image, font
    i = 1
    clear_canvas()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    menu_image.clip_draw(235, 290, 245, 180, get_canvas_width() // 2, get_canvas_height() // 2, 245 * 2, 180 * 2)
    menu_image.clip_draw(188, 223, 138, 50, get_canvas_width() // 2, get_canvas_height() // 2 + 200, 138 * 3, 50 * 2)
    font.draw(get_canvas_width() // 2 - 150, get_canvas_height() // 2 + 200, 'HIGH SCORE', (200, 0, 0))
    for sd in sorted_data:
        font.draw(get_canvas_width()//2 - 200, get_canvas_height()//2 + 200 - i * 100, f"{i}.{sd['name'][0]}{sd['name'][1]}{sd['name'][2]}:{sd['score']}", (251, 250, 180))
        i += 1
        if i == 4:
            break
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            else:
                game_framework.change_state(title_state)
