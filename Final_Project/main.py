import play_state
import pico2d
import title_state
import logo_state

start_state = [logo_state, title_state, play_state]
pico2d.open_canvas(800, 950)


for state in start_state:
    state.enter()  # initialize
    # game loop
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()   # exit

pico2d.close_canvas()