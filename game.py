import pygame
import serial

pygame.init()

ser = serial.Serial('COM3', 115200, timeout=1)

bg = pygame.image.load('8209_exb9_210318.jpg')
bg = pygame.transform.scale(bg, (700, 350))
bg_width, bg_height = bg.get_width(), bg.get_height()
car = pygame.image.load('car.png')
car = pygame.transform.scale(car, (300, 350))

screen = pygame.display.set_mode((bg_width, bg_height))


shift = 0

run = True


while run:

    a = ser.readline().decode('utf-8').strip()
    if a:
        a_number = float(a)
    else:
        a_number = 0

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if(key[pygame.K_LEFT] or (a_number) > 5):
        shift -= 2

    if(key[pygame.K_RIGHT] or (a_number) < -5):
        shift += 2
        
    if(key[pygame.K_UP]):
        shift += 2
           
    if(key[pygame.K_DOWN]):
        shift -= 2

    

    if(shift > bg_width):
        shift = 0
    if(shift < 0):
        shift = bg_width
    
    
    screen.blit(bg, (-shift,0))
    screen.blit(bg, (-shift + bg_width,0))
    screen.blit(car, (0,130))
    

    pygame.display.update()

pygame.quit()