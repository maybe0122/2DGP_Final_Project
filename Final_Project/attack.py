from pico2d import *
import game_world
import game_framework

# Attack Speed
PIXEL_PER_METER = (10.0 / 0.3)
A_SPEED_KMPH = 15.0
A_SPEED_MPM = (A_SPEED_KMPH * 1000.0 / 60.0)
A_SPEED_MPS = (A_SPEED_MPM / 60.0)
A_SPEED_PPS = (A_SPEED_MPS * PIXEL_PER_METER)

# Enemy Attack Speed
E_SPEED_KMPH = 25.0
E_SPEED_MPM = (E_SPEED_KMPH * 1000.0 / 60.0)
E_SPEED_MPS = (E_SPEED_MPM / 60.0)
E_SPEED_PPS = (E_SPEED_MPS * PIXEL_PER_METER)


class Attack:
    image = None

    def __init__(self, x=740, y=450, velocity=1):
        if self.image == None:
            self.image = load_image('source/image/basic_fire.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.clip_composite_draw(370, 134 - 50, 80, 50, 3.141592 / 2, '', self.x, self.y + 64, 40, 20)
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.velocity * A_SPEED_PPS * game_framework.frame_time

        if self.y > 900:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 20 + 64, self.x + 10, self.y + 20 + 64

    def handle_collision(self, other, group):
        if group == 'attack:enemy':
            for layer in game_world.objects:        # 적이 겹쳐있을 경우 공격이 이미 삭제되었다면 삭제하지 않도록 구현
                if self in layer:
                    game_world.remove_object(self)
        elif group == 'attack:enemy_attack':
            game_world.remove_object(self)


class Enemy_Attack:
    image = None

    def __init__(self, x=740, y=450, velocity=1):
        if Enemy_Attack.image == None:
            Enemy_Attack.image = load_image('source/image/aircrafts.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.damage = 10

    def draw(self):
        self.image.clip_draw(450, 891, 11, 11, self.x, self.y - 45, 22, 22)
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.velocity * E_SPEED_PPS * game_framework.frame_time

        if self.y < 0:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 11, self.y - 11 - 45, self.x + 11, self.y + 11 - 45

    def handle_collision(self, other, group):
        if group == 'player:enemy_attack':
            other.health -= 10
            game_world.remove_object(self)
        elif group == 'attack:enemy_attack':
            game_world.remove_object(self)
