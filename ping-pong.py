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

class Player(GameSprite):
    def __init__(self, speed, picture, x, y):
        super().__init__(speed, picture, x, y)
        self.image = transform.scale(image.load(picture), (80, 160))
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self, speed, picture, x, y):
        super().__init__(speed, picture, x, y)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player1 = Player(5, 'tennis_racket.png', 20, 200)
player2 = Player(5, 'tennis_racket.png', 600, 200)
ball = Ball(8, 'png_tennis_ball.png', 350, 250)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((220, 232, 112))
    player1.reset()
    player2.reset()
    ball.reset()

    clock.tick(60)
    display.update()
