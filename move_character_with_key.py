from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('character.png')


def handle_events():
    global running, x, y, move_x, move_y

    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.type == SDLK_RIGHT:
                move_x += 1
            elif event.type == SDLK_LEFT:
                move_x -= 1
            elif event.type == SDLK_UP:
                move_y += 1
            elif event.type == SDLK_DOWN:
                move_y -= 1
        elif event.type == SDL_KEYUP:
            if event.type == SDLK_RIGHT:
                move_x = 0
            elif event.type == SDLK_LEFT:
                move_x = 0
            elif event.type == SDLK_UP:
                move_y = 0
            elif event.type == SDLK_DOWN:
                move_y = 0

    x += move_x * 5
    y += move_y * 5

    if x<0:
        x=0
    elif x>TUK_WIDTH:
        x= TUK_WIDTH-64

    if y<0:
        y=0
    elif y>TUK_HEIGHT:
        y= TUK_HEIGHT-64



running = True
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
move_x=0
move_y=0
frame = 0

while running:
    clear_canvas()
    background.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    character.clip_draw(frame * 64, 64, 64, 64, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    delay(0.01)
close_canvas()

