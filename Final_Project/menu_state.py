from pico2d import *
import game_framework
import title_state
import play_state

image = None
font = None

def enter():
    global image, font
    image = load_image('source/image/menu.png')
    font = load_font('source/font/ENCR10B.TTF')

def exit():
    global image, font
    del image, font

def update():
    pass

def draw():
    global image, font
    clear_canvas()
    play_state.draw_world()
    image.clip_draw(235, 290, 245, 180, get_canvas_width() // 2, get_canvas_height() // 2, 245 * 2, 180 * 2)
    image.clip_draw(188, 223, 138, 50, get_canvas_width() // 2, get_canvas_height() // 2 + 100, 138 * 2.5, 50 * 1.5)
    image.clip_draw(188, 223, 138, 50, get_canvas_width() // 2, get_canvas_height() // 2, 138 * 2.5, 50 * 1.5)
    image.clip_draw(188, 223, 138, 50, get_canvas_width() // 2, get_canvas_height() // 2 - 100, 138 * 2.5, 50 * 1.5)
    # 폰트 위치 수정하기
    font.draw(get_canvas_width()//2 - 100, get_canvas_height()//2 + 100, 'B : Back to Play', (255, 0, 0))
    font.draw(get_canvas_width()//2 - 100, get_canvas_height()//2, 'R : Play New Game', (255, 0, 0))
    font.draw(get_canvas_width()//2 - 100, get_canvas_height()//2 - 100, 'ESC : Back to title', (255, 0, 0))
    update_canvas()

def handle_events():
    global new
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:    # move to title
                    game_framework.change_state(title_state)
                case pico2d.SDLK_b:  # resume game
                    game_framework.pop_state()
                case pico2d.SDLK_r:  # restart game
                    game_framework.change_state(play_state)

def pause():
    pass

def resume():
    pass