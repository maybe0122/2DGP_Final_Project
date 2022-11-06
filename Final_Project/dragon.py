from pico2d import *
import game_world

# 이벤트 정의
AD, AU, SD, SU, DD, DU, WD, WU = range(8)

key_event_table = {
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
        print('Enter Idle')

    @staticmethod
    def exit(self, event):
        print('Exit Idle')

    @staticmethod
    def do(self):
        self.frame = (self.fram + 1) % 3

    @staticmethod
    def draw(self):
        self.image.clip_draw(self.frame * 144, 128 * 3, 144, 128, self.x, self.y)

class MOVE:
    def enter(self, event):
        print('Enter Move')
        if event == AU:
            pass
        elif event == AD:
            pass
        elif event == WU:
            pass
        elif event == WD:
            pass
        elif event == SU:
            pass
        elif event == SD:
            pass
        elif event == DU:
            pass
        elif event == DD:
            pass

    def exit(self, event):
        print('Exit Move')

    def do(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dir_x
        self.y += self.dir_y
        self.x = clamp(0 + 72, self.x, 800 - 72)
        self.y = clamp(0 + 54, self.y, 950 - 54)

    def draw(self):
        self.image.clip_draw(self.frame * 144, 128 * 3, 144, 128, self.x, self.y)


# 상태 변환
next_state = {
    IDLE: {WU: MOVE, WD: MOVE, AU: MOVE, AD: MOVE, SU: MOVE, SD: MOVE, DU: MOVE, DD: MOVE},
    MOVE: {}
}

class Dragon:
    def __init__(self):
        self.x, self.y = 800 // 2, 64
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.image = load_image('source/image/flying_dragon-red.png')

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

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)