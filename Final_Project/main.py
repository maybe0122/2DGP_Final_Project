import play_state
import pico2d
import title_state
import logo_state
import game_framework

# start_state = [logo_state, title_state, play_state]
states = [logo_state]
pico2d.open_canvas(740, 800)


# for state in start_state:
#     state.enter()  # initialize
#     # game loop
#     while state.running:
#         state.handle_events()
#         state.update()
#         state.draw()
#     state.exit()   # exit

for state in states:
    game_framework.run(state)

pico2d.close_canvas()
