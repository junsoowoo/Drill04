from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, x, y, move_x, move_y, dire, move_frame, idle_frame

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                move_x += 1
                dire = 1
            elif event.key == SDLK_LEFT:
                move_x -= 1
                dire = 0
            elif event.key == SDLK_UP:
                move_y += 1
                dire = 2
            elif event.key == SDLK_DOWN:
                move_y -= 1
                dire = 3
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                move_x = 0
            elif event.key == SDLK_LEFT:
                move_x = 0
            elif event.key == SDLK_UP:
                move_y = 0
            elif event.key == SDLK_DOWN:
                move_y = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    if x < 0:
        x = 0
    elif x > TUK_WIDTH:
        x = TUK_WIDTH - 64

    if y < 0:
        y = 0
    elif y > TUK_HEIGHT:
        y = TUK_HEIGHT - 64

running = True
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
move_x, move_y ,move_frame= 0, 0, 0
dire = 1

while running:
    clear_canvas()
    background.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    x += move_x * 5
    y += move_y * 5
    character.clip_draw(move_frame * 100, dire * 0, 100, 100, x, y)
    update_canvas()
    move_frame = (move_frame + 1) % 10
    handle_events()

close_canvas()

