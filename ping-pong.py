from pygame import *
font.init()

window = display.set_mode((700, 500))

clock = time.Clock()

font = font.Font(None, 35)
win_p1 = font.render('Player 1 win!', True, (250, 246, 14))
win_p2 = font.render('Player 2 win!', True, (250, 246, 14))
speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, speed, picture, x, y):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(picture), (60, 60))
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

player1 = Player1(4, 'tennis_racket.png', -15, 200)
player2 = Player2(4, 'tennis_racket.png', 600, 200)
ball = GameSprite(7.5, 'tennis_ball.png', 350, 250)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        
        window.fill((220, 232, 112))

        ball.rect.y += speed_y
        ball.rect.x += speed_x
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        
        if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(win_p2, (300,240))
            clock.tick(60)
            display.update()
        
        if ball.rect.x > 640:
            finish = True
            window.blit(win_p1, (300,240))
            clock.tick(60)
            display.update()

        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()

        clock.tick(60)
        display.update()
