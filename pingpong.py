from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()        
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_height - 80:
            self.rect.y += self.speed

            

#escena del videojuego: 
back = (200, 255, 255) #Fondo azul claro
window_width = 600
window_height = 500
window = display.set_mode((window_width, window_height)) 
window.fill(back)

game = True 
finish = False 
clock = time.Clock() 
FPS = 60 

speed_x = 3
speed_y = 3

while game:
    display.update()
    clock.tick(FPS)
