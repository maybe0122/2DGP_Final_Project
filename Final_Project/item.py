from pico2d import *

import background
import dragon
import game_world
import game_framework
import random
import play_state
from attack import Attack

# item type
# 0 : 체력 회복
# 1 : 이동 속도 증가
# 2 : 데미지 증가
# 3 : 추가 점수


# item fall Speed
PIXEL_PER_METER = (10.0 / 0.3)
A_SPEED_KMPH = 20.0
A_SPEED_MPM = (A_SPEED_KMPH * 1000.0 / 60.0)
A_SPEED_MPS = (A_SPEED_MPM / 60.0)
A_SPEED_PPS = (A_SPEED_MPS * PIXEL_PER_METER)

class Item:
    image = None

    def __init__(self, x=740, y=450, velocity=1):
        if Item.image == None:
            Item.image = load_image('source/image/item_set.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.type = random.randint(0, 3)

    def draw(self):
        if self.type == 0:
            self.image.clip_draw(136, 353 - 109, 64, 64, self.x, self.y, 32, 32)
        elif self.type == 1:
            self.image.clip_draw(41, 353 - 109, 64, 64, self.x, self.y, 32, 32)
        elif self.type == 2:
            self.image.clip_draw(326, 353 - 305, 64, 64, self.x, self.y, 32, 32)
        elif self.type == 3:
            self.image.clip_draw(513, 353 - 305, 64, 64, self.x, self.y, 32, 32)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.velocity * A_SPEED_PPS * game_framework.frame_time

        if self.y < 0:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 15, self.y + 14

    def handle_collision(self, other, group):
        if group == 'player:item':
            if self.type == 0:
                if other.health != dragon.MAX_HEALTH:  # 플레이어가 최대 체력이 아닐 경우 10 회복
                    other.health += 10
            elif self.type == 1:
                other.speed += 0.01
                # print(other.speed)
            elif self.type == 2:
                play_state.player.player_damage += 10    # 데미지 조정 필요
                # print(play_state.player.player_damage)
            elif self.type == 3:
                play_state.player.score += random.randint(1, 6) * 100  # 100 ~ 500까지의 랜덤 점수 획득
            game_world.remove_object(self)
