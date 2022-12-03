import pico2d
import game_framework

import logo_state
import play_state
import title_state
import save_score_state
import game_over_state

pico2d.open_canvas(740, 900)
game_framework.run(play_state)  # test state
pico2d.close_canvas()
