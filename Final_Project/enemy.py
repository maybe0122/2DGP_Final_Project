from pico2d import *
import game_world
import random
import background
from item import Item
from explosion import Explosion
import game_framework

import play_state
from attack import Attack, Breath


class Enemy1:
    image = None

    def __init__(self, x=random.randint(55, 750 - 55), y=800-90):
        self.x, self.y = x, y
        self.dir_x = 0
        self.dir_y = 0
        self.health = 50
        self.enemy_damage = 10
        self.face_dir = -1

        if Enemy1.image == None:
            Enemy1.image = load_image('source/image/aircrafts.png')

    def draw(self):
        self.image.clip_composite_draw(0, 1024 - 190, 110, 90, 0, 'v', self.x, self.y, 100, 90)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def drop_item(self):
        play_state.items = Item(self.x, self.y, self.face_dir*2)
        game_world.add_object(play_state.items, 1)
        game_world.add_collision_pairs(None, play_state.items, 'player:item')

    def explosion_animation(self):
        play_state.explosions = Explosion(self.x, self.y)
        game_world.add_object(play_state.explosions, 1)

    def get_bb(self):
        return self.x - 55, self.y - 45, self.x + 55, self.y + 45

    def handle_collision(self, other, group):
        if group == 'player:enemy':
            game_world.remove_object(self)
        elif group == 'attack:enemy':       # self : enemy, other : attack
            self.health -= play_state.player.player_damage
            if self.health <= 0:
                play_state.player.score += 100
                game_world.remove_object(self)
                self.explosion_animation()
                self.drop_item()

class Enemy2:
    image = None

    def __init__(self):
        random.randint(0, 740), 800 - 50
        self.dir_x = 0
        self.dir_y = 0

        if self.image == None:
            Enemy2.image = load_image('source/image/aircrafts.png')
    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'player:enemy':
            game_world.remove_object(self)

class Enemy3:
    image = None

    def __init__(self):
        random.randint(0, 740), 800 - 50
        self.dir_x = 0
        self.dir_y = 0

        if self.image == None:
            Enemy3.image = load_image('source/image/aircrafts.png')

    def draw(self):
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'player:enemy':
            game_world.remove_object(self)
