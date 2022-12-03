from pico2d import *
import game_world
import game_framework

# explosion Frame Speed
TIMER_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION
FRAMES_PER_ACTION = 3


class Explosion:
    explosion_image = None

    def __init__(self, x=740, y=450):
        if Explosion.explosion_image == None:
            Explosion.explosion_image = load_image('source/image/explosion.png')
        self.x, self.y, = x, y
        self.frame_x, self.frame_y = 0, 3

    def draw(self):
        self.explosion_image.clip_draw(int(self.frame_x) * 192, int(self.frame_y) * 192, 192, 192, self.x, self.y)

    def update(self):
        if self.frame_y >= 0:
            self.frame_x = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            if int(self.frame_x) == 4:
                self.frame_y -= 1
        else:
            game_world.remove_object(self)

