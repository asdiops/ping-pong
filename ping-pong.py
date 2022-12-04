from pygame import *

window = display.set_mode((700, 500))

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, speed, picture, x, y):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(picture), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def __init__(self, speed, picture, x, y):
        super().__init__(speed, picture, x, y)
        self.image = transform.scale(image.load(picture), (140, 160))
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y != 0:
            self.rect.y -= 4.5
        if keys_pressed[K_s] and self.rect.y != 340:
            self.rect.y += 4.5

class Player2(GameSprite):
    def __init__(self, speed, picture, x, y):
        super().__init__(speed, picture, x, y)
        self.image = transform.scale(image.load(picture), (140, 160))
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y != 0:
            self.rect.y -= 4.5
        if keys_pressed[K_DOWN] and self.rect.y != 340:
            self.rect.y += 4.5

class Ball(GameSprite):
    def __init__(self, speed, picture, x, y):
        super().__init__(speed, picture, x, y)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player1 = Player1(3, 'tennis_racket.png', -45, 200)
player2 = Player2(3, 'tennis_racket.png', 600, 200)
ball = Ball(8, 'tennis_ball.png', 350, 250)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((220, 232, 112))
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    ball.reset()

    clock.tick(60)
    display.update()
