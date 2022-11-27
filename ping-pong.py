from pygame import *

window = display.set_mode((700, 500))

clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((220, 232, 112))

    clock.tick(60)
    display.update()
