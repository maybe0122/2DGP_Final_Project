from pico2d import *

import game_framework
import game_world
import play_state
from attack import Attack, Breath

# Dragon Fly Speed
PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 20.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Dragon Frame Speed
TIMER_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION
FRAMES_PER_ACTION = 3


# 이벤트 정의
AD, AU, SD, SU, DD, DU, WD, WU, FIRE, BREATH = range(10)

event_name = ['AD', 'AU', 'SD', 'SU', 'DD', 'DU', 'WD', 'WU', 'FIRE', 'BREATH']

key_event_table = {
    (SDL_KEYDOWN, SDLK_j): FIRE,
    (SDL_KEYDOWN, SDLK_k): BREATH,
    (SDL_KEYDOWN, SDLK_w): WD,
    (SDL_KEYDOWN, SDLK_a): AD,
    (SDL_KEYDOWN, SDLK_s): SD,
    (SDL_KEYDOWN, SDLK_d): DD,
    (SDL_KEYUP, SDLK_w): WU,
    (SDL_KEYUP, SDLK_a): AU,
    (SDL_KEYUP, SDLK_s): SU,
    (SDL_KEYUP, SDLK_d): DU
}

# 상태 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        self.dir_x, self.dir_y = 0, 0

    @staticmethod
    def exit(self, event):
        if event == FIRE:
            self.basic_attack()
        elif event is BREATH:
            self.breath()
        self.dir_x, self.dir_y = 0, 0

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 144, 128 * 3, 144, 128, self.x, self.y)

class MOVE:
    def enter(self, event):
        if event == AU:
            self.dir_x += 1
        elif event == AD:
            self.dir_x -= 1
        elif event == WU:
            self.dir_y -= 1
        elif event == WD:
            self.dir_y += 1
        elif event == SU:
            self.dir_y += 1
        elif event == SD:
            self.dir_y -= 1
        elif event == DU:
            self.dir_x -= 1
        elif event == DD:
            self.dir_x += 1

    def exit(self, event):
        if event is FIRE:
            self.basic_attack()
        elif event is BREATH:
            self.breath()

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x += self.dir_x * FLY_SPEED_PPS * game_framework.frame_time
        self.y += self.dir_y * FLY_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0 + 72, self.x, 800 - 72)
        self.y = clamp(0 + 54, self.y, 950 - 54)
        # print(self.event_que)


    def draw(self):
        self.image.clip_draw(int(self.frame) * 144, 128 * 3, 144, 128, self.x, self.y)


# 상태 변환
next_state = {
    IDLE: {WU: MOVE, WD: MOVE, AU: MOVE, AD: MOVE, SU: MOVE, SD: MOVE, DU: MOVE, DD: MOVE, FIRE: IDLE, BREATH: IDLE},
    MOVE: {WU: MOVE, WD: MOVE, AU: MOVE, AD: MOVE, SU: MOVE, SD: MOVE, DU: MOVE, DD: MOVE, FIRE: MOVE, BREATH: IDLE}
}

class Dragon:
    def __init__(self):
        self.x, self.y = 800 // 2, 64
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.face_dir = 1
        self.image = load_image('source/image/flying_dragon-red.png')
        self.font = load_font('ENCR10B.TTF', 16)    # change font size later

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}  Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        # self.font.draw()

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def basic_attack(self):
        play_state.attack += [Attack(self.x, self.y, self.face_dir*2)]
        game_world.add_objects(play_state.attack, 1)
        # game_world.add_collision_pairs(play_state.attack, play_state.enemies, 'attack:enemy')

    def breath(self):
        play_state.attack += [Breath()]
        game_world.add_objects(play_state.attack, 1)

    def get_bb(self):
        return self.x - 72, self.y - 64, self.x + 72, self.y + 64

    def handle_collision(self, other, group):
        pass

