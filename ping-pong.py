#создать окно игры и прикрепить к нему фон
# #создать универсальный класс для спрайтов
#создать класс Ракетка (наследник от универсального класса)
#создать класс Мяч (наследник от универсального класса). Перемещение организовать по примеру игры арканоид.
#создать два экземпляра класса Ракетка
#создать экземпляр класса Мяч
#написать игровой цикл
#запрограммировать условия выигрыша и проигрыша

from pygame import *


#окно игры
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")

#фон сцены
background = (165, 255, 1)
window.fill(background)
#background = transform.scale(image.load(""), (win_width, win_height))

#универсальный класс игровых спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, size, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.size = size
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс Ракетка игрока (наследник от универсального класса)
class PlayerSprite(GameSprite):
    def update(self, a, b):
        buttons = [K_UP, K_DOWN, K_LSHIFT, K_LCTRL]
        keys_pressed = key.get_pressed()

        if keys_pressed[buttons[a]] and self.rect.y > win_height-480:
            self.rect.y -= self.speed
        elif keys_pressed[buttons[b]] and self.rect.y < win_height-160:
            self.rect.y += self.speed

#класс Мяч (наследник от универсального класса)
class BallSprite(GameSprite):
    def update(self, player):
        global win_width, win_height, speed_x, speed_y, finish, player_lose

        self.rect.x += speed_x
        self.rect.y += speed_y

        if self.rect.x < 0:
            finish = True
            player_lose = 'player_1'
        
        elif self.rect.x > win_width:
            finish = True
            player_lose = 'player_2'

        if self.rect.y < 0 or self.rect.y > win_height:
            speed_y *= -1
        
        if sprite.collide_rect(self, player):
            speed_x *= -1

player_1 = PlayerSprite((30, 150), 'platform.png', 60, 210, 8)
player_2 = PlayerSprite((30, 150), 'platform.png', 620, 210, 8)
ball = BallSprite((30, 30), 'ball.png', 40, 80, 4)

font.init()
font_new = font.SysFont('Arial', 70)

clock = time.Clock()
FPS = 60
speed_x = ball.speed
speed_y = ball.speed
game_over = False
finish = False
player_lose = ''

while game_over == False:
    for e in event.get():
        if e.type == QUIT:
            game_over = True

    if finish == False:
        window.fill(background)

        player_1.update(2, 3)
        player_1.reset()

        player_2.reset()
        player_2.update(0, 1)

        ball.reset()
        ball.update(player_1)
        ball.update(player_2)

    else:
        lose = font_new.render((player_lose+' lose!'), True, (180, 0, 0))
        window.blit(lose, (230, 200))

    display.update()
    clock.tick(FPS)