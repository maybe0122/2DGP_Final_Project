import toml
from pico2d import *
import game_framework
import game_world
import menu_state
import random
import pickle
import enemy
from dragon import Dragon
from enemy import Enemy1, Enemy2
from background import Background


player = None
enemies = None
background = None
attacks = None
items = None
explosions = None
enemy_attacks = None

wave_counter = 1
enemy_counter = 0

wave1 = [
    {'name': 'Enemy1', 'x': 74, 'y': 750},
    {'name': 'Enemy1', 'x': 74 + 148, 'y': 750},
    {'name': 'Enemy1', 'x': 74 + 148 * 2, 'y': 750},
    {'name': 'Enemy1', 'x': 74 + 148 * 3, 'y': 750},
    {'name': 'Enemy1', 'x': 74 + 148 * 4, 'y': 750}
]

wave2 = [
    {'name': "Enemy1", 'x': 123, 'y': 750},
    {'name': "Enemy1", 'x': 369, 'y': 750},
    {'name': "Enemy1", 'x': 615, 'y': 750},
    {'name': "Enemy2", 'x': 123, 'y': 1600},
    {'name': "Enemy2", 'x': 369, 'y': 1600},
    {'name': "Enemy2", 'x': 615, 'y': 1600}
]

wave3 = [
    {'name': "Enemy2", 'x': 74, 'y': 1600},
    {'name': "Enemy2", 'x': 74 + 148, 'y': 1400},
    {'name': "Enemy2", 'x': 74 + 148 * 2, 'y': 1200},
    {'name': "Enemy2", 'x': 74 + 148 * 3, 'y': 1400},
    {'name': "Enemy2", 'x': 74 + 148 * 4, 'y': 1600}
]

boss = [
    {'name': 'Boss', 'x': 0, 'y': 0}
]

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(menu_state)   # press esc to move menu
        else:
            player.handle_event(event)


def enter():
    global player, enemies, background, enemy_counter, wave_counter

    enemy_counter = 0
    wave_counter = 0

    # 객체 생성
    player = Dragon()
    background = Background()

    # 게임 월드에 객체 추가
    game_world.add_object(player, 1)
    game_world.add_object(background, 0)

    load_enemy(wave1)

    # 충돌 그룹 추가
    game_world.add_collision_pairs(player, None, 'player:item')
    game_world.add_collision_pairs(player, None, 'player:enemy_attack')
    game_world.add_collision_pairs(None, None, 'attack:enemy_attack')


def exit():
    game_world.clear()


def load_enemy(wave):
    global enemies, enemy_counter
    for o in wave:
        if o['name'] == 'Enemy1':
            enemies = Enemy1(o['x'], o['y'])
            game_world.add_object(enemies, 1)
            game_world.add_collision_pairs(player, enemies, 'player:enemy')
            game_world.add_collision_pairs(None, enemies, 'attack:enemy')
            enemy_counter += 1
        elif o['name'] == 'Enemy2':
            enemies = Enemy2(o['x'], o['y'])
            game_world.add_object(enemies, 1)
            game_world.add_collision_pairs(player, enemies, 'player:enemy')
            game_world.add_collision_pairs(None, enemies, 'attack:enemy')
            enemy_counter += 1
        # elif o['name'] == 'Boss':
        #     enemies = Boss(o['x'], o['y'])
        #     game_world.add_object(enemies, 1)
        #     game_world.add_collision_pairs(player, enemies, 'player:enemy')
        #     game_world.add_collision_pairs(None, enemies, 'attack:enemy')
        #     enemy_counter += 1

def update():
    global wave_counter
    for game_object in game_world.all_object():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    if enemy_counter == 0:
        n = random.randint(0, 3)
        if n == 0:
            load_enemy(wave1)
        if n == 1:
            load_enemy(wave2)
        if n == 2:
            load_enemy(wave3)
        wave_counter += 1

    # if wave_counter % 10 == 0:
    #     load_enemy(boss)


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    for game_object in game_world.all_object():
        game_object.draw()


def pause():
    pass


def resume():
    pass


def test_self():
    import play_state

    pico2d.open_canvas(800, 950)
    game_framework.run(play_state)
    pico2d.clear_canvas()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


if __name__ == '__main__':
    test_self()
