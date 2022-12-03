import pico2d
import logo_state
import game_framework

states = [logo_state]
pico2d.open_canvas(740, 900)

for state in states:
    game_framework.run(state)

pico2d.close_canvas()
