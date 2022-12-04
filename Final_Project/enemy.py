from pico2d import *
import game_world
import random
from item import Item
from explosion import Explosion
import game_framework
from attack import Enemy_Attack
import play_state

# Enemy2 Speed
PIXEL_PER_METER = (10.0 / 0.3)
A_SPEED_KMPH = 50.0
A_SPEED_MPM = (A_SPEED_KMPH * 1000.0 / 60.0)
A_SPEED_MPS = (A_SPEED_MPM / 60.0)
A_SPEED_PPS = (A_SPEED_MPS * PIXEL_PER_METER)


class Enemy1:
    image = None
    ex_sound = None

    def __init__(self, x=random.randint(55, 750 - 55), y=800-90):
        self.x, self.y = x, y
        self.health = 50
        self.enemy_damage = 10
        self.face_dir = -1
        self.timer = 20

        if Enemy1.ex_sound == None:
            Enemy1.ex_sound = load_wav('source/sound/explosion.wav')
            Enemy1.ex_sound.set_volume(32)

        if Enemy1.image == None:
            Enemy1.image = load_image('source/image/aircrafts.png')

    def draw(self):
        self.image.clip_composite_draw(0, 1024 - 190, 110, 90, 0, 'v', self.x, self.y, 100, 90)
        if self.timer <= 0:
            self.basic_attack()
            self.timer = 20
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.timer > 0:
            self.timer -= 0.1

    def drop_item(self):
        play_state.items = Item(self.x, self.y, self.face_dir*2)
        game_world.add_object(play_state.items, 1)
        game_world.add_collision_pairs(None, play_state.items, 'player:item')

    def explosion_animation(self):
        play_state.explosions = Explosion(self.x, self.y)
        game_world.add_object(play_state.explosions, 1)

    def basic_attack(self):
        play_state.enemy_attacks = Enemy_Attack(self.x, self.y, self.face_dir * 2)
        game_world.add_object(play_state.enemy_attacks, 1)
        game_world.add_collision_pairs(None, play_state.enemy_attacks, 'player:enemy_attack')
        game_world.add_collision_pairs(None, play_state.enemy_attacks, 'attack:enemy_attack')

    def get_bb(self):
        return self.x - 55, self.y - 45, self.x + 55, self.y + 45

    def handle_collision(self, other, group):
        if group == 'player:enemy':
            play_state.enemy_counter -= 1
            game_world.remove_object(self)
        elif group == 'attack:enemy':       # self : enemy, other : attack
            self.health -= play_state.player.player_damage
            if self.health <= 0:
                play_state.enemy_counter -= 1
                play_state.player.score += 100
                Enemy1.ex_sound.play()
                game_world.remove_object(self)
                self.explosion_animation()
                self.drop_item()

class Enemy2:
    image = None
    ex_sound = None

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.health = 20
        self.enemy_damage = 10
        self.face_dir = -1
        self.timer = 20

        if Enemy2.ex_sound == None:
            Enemy2.ex_sound = load_wav('source/sound/explosion.wav')
            Enemy2.ex_sound.set_volume(32)

        if Enemy2.image == None:
            Enemy2.image = load_image('source/image/aircrafts.png')
    def draw(self):
        self.image.clip_composite_draw(225, 1024 - 90, 110, 90, 0, 'v', self.x, self.y, 100, 90)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.face_dir * A_SPEED_PPS * game_framework.frame_time

        if self.y < 0:
            play_state.enemy_counter -= 1
            game_world.remove_object(self)

    def drop_item(self):
        play_state.items = Item(self.x, self.y, self.face_dir * 2)
        game_world.add_object(play_state.items, 1)
        game_world.add_collision_pairs(None, play_state.items, 'player:item')

    def explosion_animation(self):
        play_state.explosions = Explosion(self.x, self.y)
        game_world.add_object(play_state.explosions, 1)

    def get_bb(self):
        return self.x - 55, self.y - 45, self.x + 55, self.y + 45

    def handle_collision(self, other, group):
        if group == 'player:enemy':
            play_state.enemy_counter -= 1
            game_world.remove_object(self)
        elif group == 'attack:enemy':  # self : enemy, other : attack
            self.health -= play_state.player.player_damage
            if self.health <= 0:
                play_state.enemy_counter -= 1
                play_state.player.score += 100
                Enemy2.ex_sound.play()
                game_world.remove_object(self)
                self.explosion_animation()
                self.drop_item()

class Boss:
    image = None

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.dir_x = 0
        self.dir_y = 0

        if Boss.image == None:
            Boss.image = load_image('source/image/boss.png')

    def draw(self):
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'player:enemy':
            game_world.remove_object(self)
