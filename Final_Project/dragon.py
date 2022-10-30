from pico2d import *
import game_framework

class Dragon:
    def __init__(self):
        self.x, self.y = 800 // 2, 64
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.image = load_image('source/image/flying_dragon-red.png')

    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
        self.x = clamp(0 + 72, self.x, 800 - 72)
        self.y = clamp(0 + 54, self.y, 950 - 54)


    def draw(self):
        self.image.clip_draw(self.frame * 144, 128 * 3, 144, 128, self.x, self.y)

def handle_events(self, event):
    if event.type == SDL_KEYDOWN:
        if event.key == SDLK_w:  # up
            self.dir_y += 1
        elif event.key == SDLK_a:  # left
            self.dir_x -= 1
        elif event.key == SDLK_s:  # down
            self.dir_y -= 1
        elif event.key == SDLK_d:  # right
            self.dir_x += 1
    elif event.type == SDL_KEYUP:
        if event.key == SDLK_w:  # up
            self.dir_y -= 1
        elif event.key == SDLK_a:  # left
            self.dir_x += 1
        elif event.key == SDLK_s:  # down
            self.dir_y += 1
        elif event.key == SDLK_d:  # right
            self.dir_x -= 1
