from pico2d import *
import game_framework

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:    # move to title
                    game_framework.pop_state()
                case pico2d.SDLK_b:  # resume game
                    pass
                case pico2d.SDLK_r:  # restart game
                    pass