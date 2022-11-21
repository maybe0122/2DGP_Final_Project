from pico2d import *
import game_world
import game_framework

# Attack Speed
PIXEL_PER_METER = (10.0 / 0.3)
A_SPEED_KMPH = 15.0
A_SPEED_MPM = (A_SPEED_KMPH * 1000.0 / 60.0)
A_SPEED_MPS = (A_SPEED_MPM / 60.0)
A_SPEED_PPS = (A_SPEED_MPS * PIXEL_PER_METER)

class Attack:
    image = None

    def __init__(self, x=740, y=450, velocity=1):
        if self.image == None:
            self.image = load_image('source/image/basic_fire.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.damage = 10

    def draw(self):
        self.image.clip_composite_draw(370, 134 - 50, 80, 50, 3.141592 / 2, '', self.x, self.y + 64, 40, 20)
        draw_rectangle(*self.get_bb())

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

class Breath:
    image = None

    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass

    def get_bb(self):
        pass

    def handle_collision(self, other, group):
        pass

class Enemy_Attack:
    image = None

    def __init__(self, x=740, y=450, velocity=1):
        if Enemy_Attack.image == None:
            Enemy_Attack.image = load_image('source/image/basic_fire.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.damage = 10

    def draw(self):
        self.image.clip_composite_draw(370, 134 - 50, 80, 50, 3.141592 / 2, '', self.x, self.y + 64, 40, 20)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.velocity * A_SPEED_PPS * game_framework.frame_time

        if self.y < 0:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 20 + 64, self.x + 10, self.y + 20 + 64

    def handle_collision(self, other, group):
        if group == 'player:attack':
            pass
