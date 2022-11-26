from pico2d import *
import game_framework
import title_state
import play_state

image = None

def enter():
    global image
    image = load_image('source/image/menu.png')  # add image later

def exit():
    global image
    del image

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(800, 950)
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