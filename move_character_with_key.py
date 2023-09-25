from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
background = load_image('TUK_GROUD.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running

    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        if event.type == SDL_KEYDOWN:
            if event.type == SDLK_RIGHT:
                pass
            elif event.type == SDLK_LEFT:
                pass
            elif event.type == SDLK_UP:
                pass
            elif event.type == SDLK_DOWN:
                pass



running = True
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
move_x=0
move_y=0
frame = 0

while running:
    clear_canvas()
    background.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8


close_canvas()

