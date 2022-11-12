from pico2d import *
import game_framework
import game_world

from dragon import Dragon
from enemy import Enemy1 #, Enemy2, Enemy3
from background import Background
from attack import Attack

import title_state
import menu_state
import random
import count_state


player = None
enemies = []
background = None
attack = []
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
    global player, enemies, background, attack

    # 객체 생성
    player = Dragon()
    enemies = [Enemy1() for _ in range(2)] # + [Enemy2() for _ in range(2)] + [Enemy3() for _ in range(2)]
    background = Background()

    # 게임 월드에 객체 추가
    game_world.add_object(player, 1)
    game_world.add_objects(enemies, 1)
    game_world.add_object(background, 0)


    # 충돌 그룹 추가

    game_world.add_collision_pairs(player, enemies, 'player:enemy')
    game_world.add_collision_pairs(attack, enemies, 'attack:enemy')


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_object():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

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
