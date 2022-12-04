from pico2d import *
import play_state
import pickle
import game_framework
import high_score_state

font = None
image = None
menu_image = None
name = []
name_count = 0
score = None
data = dict()


def enter():
    global font, image, score, menu_image
    font = load_font('source/font/ENCR10B.TTF', 50)
    image = load_image('source/image/background1.png')
    menu_image = load_image('source/image/menu.png')
    score = play_state.player.score


def exit():
    global font, image, menu_image
    del font, image, menu_image


def update():
    global name_count, name
    if name_count == 4:
        name_count = 0
        save()
        name = []
        game_framework.change_state(high_score_state)


def draw():
    global image, menu_image, font
    clear_canvas()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)

    menu_image.clip_draw(235, 290, 245, 180, get_canvas_width() // 2, get_canvas_height() // 2, 245 * 2, 180 * 2)
    font.draw(get_canvas_width() // 2 - 200, get_canvas_height() // 2 + 70, f'SCORE:{score}', (251, 250, 180))
    font.draw(get_canvas_width() // 2 - 200, get_canvas_height() // 2 - 40, 'NAME : _ _ _', (251, 250, 180))
    if name_count == 1:
        font.draw(get_canvas_width() // 2 + 10, get_canvas_height() // 2 - 40, f'{name[0]}', (255, 255, 255))
    if name_count == 2:
        font.draw(get_canvas_width() // 2 + 10, get_canvas_height() // 2 - 40, f'{name[0]}', (255, 255, 255))
        font.draw(get_canvas_width() // 2 + 70, get_canvas_height() // 2 - 40, f'{name[1]}', (255, 255, 255))
    if name_count == 3:
        font.draw(get_canvas_width() // 2 + 10, get_canvas_height() // 2 - 40, f'{name[0]}', (255, 255, 255))
        font.draw(get_canvas_width() // 2 + 70, get_canvas_height() // 2 - 40, f'{name[1]}', (255, 255, 255))
        font.draw(get_canvas_width() // 2 + 130, get_canvas_height() // 2 - 40, f'{name[2]}', (255, 255, 255))

    update_canvas()


def handle_events():
    global name, name_count

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_RETURN:
                if name_count >= 3:
                    name_count += 1
            elif event.key == SDLK_SPACE:
                if name_count >= 3:
                    name_count += 1
            elif event.key == SDLK_a:
                name.append('A')
                name_count += 1
            elif event.key == SDLK_b:
                name.append('B')
                name_count += 1
            elif event.key == SDLK_c:
                name.append('C')
                name_count += 1
            elif event.key == SDLK_d:
                name.append('D')
                name_count += 1
            elif event.key == SDLK_e:
                name.append('E')
                name_count += 1
            elif event.key == SDLK_f:
                name.append('F')
                name_count += 1
            elif event.key == SDLK_g:
                name.append('G')
                name_count += 1
            elif event.key == SDLK_h:
                name.append('H')
                name_count += 1
            elif event.key == SDLK_i:
                name.append('I')
                name_count += 1
            elif event.key == SDLK_j:
                name.append('J')
                name_count += 1
            elif event.key == SDLK_k:
                name.append('K')
                name_count += 1
            elif event.key == SDLK_l:
                name.append('L')
                name_count += 1
            elif event.key == SDLK_m:
                name.append('M')
                name_count += 1
            elif event.key == SDLK_n:
                name.append('N')
                name_count += 1
            elif event.key == SDLK_o:
                name.append('O')
                name_count += 1
            elif event.key == SDLK_p:
                name.append('P')
                name_count += 1
            elif event.key == SDLK_q:
                name.append('Q')
                name_count += 1
            elif event.key == SDLK_r:
                name.append('R')
                name_count += 1
            elif event.key == SDLK_s:
                name.append('S')
                name_count += 1
            elif event.key == SDLK_t:
                name.append('T')
                name_count += 1
            elif event.key == SDLK_u:
                name.append('U')
                name_count += 1
            elif event.key == SDLK_v:
                name.append('V')
                name_count += 1
            elif event.key == SDLK_w:
                name.append('W')
                name_count += 1
            elif event.key == SDLK_x:
                name.append('X')
                name_count += 1
            elif event.key == SDLK_y:
                name.append('Y')
                name_count += 1
            elif event.key == SDLK_z:
                name.append('Z')
                name_count += 1


def save():
    global data
    data = {'score': score, 'name': name}
    with open('game.sav', 'wb') as f:
        pickle.dump(data, f)


def load():
    with open('game.sav', 'rb') as f:
        out_data = pickle.load(f)
    return out_data
