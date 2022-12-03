from pico2d import *
import background
import game_framework
import title_state
import save_score_state

font = None
image = None
score = None
name = None
data = []
sorted_data = []


def enter():
    global font, image, data, sorted_data
    font = load_font('source/font/ENCR10B.TTF', 50)
    image = load_image('source/image/background1.png')
    data.append(save_score_state.load())
    sorted_data = sorted(data, key=lambda d: d['score'], reverse=True)


def exit():
    global font, image
    del font, image


def update():
    pass


def draw():
    global image
    i = 1
    clear_canvas()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    font.draw(get_canvas_width()//2, get_canvas_height()//2, 'HIGH SCORE', (0, 0, 0))
    for sd in sorted_data:
        font.draw(get_canvas_width()//2 - 300, get_canvas_height()//2 - i * 40, f"{i}. {sd['name'][0]} {sd['name'][1]} {sd['name'][2]} | {sd['score']}")
        i += 1
        if i == 11:
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
