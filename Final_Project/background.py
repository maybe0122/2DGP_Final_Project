from pico2d import *
import play_state
import game_framework

# Map Scroll Speed
PIXEL_PER_METER = (10.0 / 0.3)
SCROLL_SPEED_KMPH = 30.0
SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)


class Background:
    def __init__(self):
        self.image = load_image('source/image/background1.png')
        self.font = load_font('source/font/ENCR10B.TTF', 30)
        self.x, self.y = get_canvas_width() // 2, get_canvas_height() // 2
        self.y2 = get_canvas_height() // 2 + 986
        self.speed = SCROLL_SPEED_PPS
        # self.bgm = load_music()
        # self.bgm.set_volume(32)
        # self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x, self.y2)
        self.font.draw(5, 900 - 10, f'Score : {play_state.player.score}', (255, 0, 0))

    def update(self):
        self.y -= 1 * self.speed * game_framework.frame_time
        self.y2 -= 1 * self.speed * game_framework.frame_time

        if self.y <= -(986 // 2):
            self.y = 986 + 986 // 2
        if self.y2 <= -(986 // 2):
            self.y2 = 986 + 986 // 2
