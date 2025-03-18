import pygame
import time

pygame.init()

clock_img = pygame.image.load('clock.png')
minute_img = pygame.image.load('minute.png')
second_img = pygame.image.load('second.png')

scale = 0.4 #decreasing size of all images
clock_img = pygame.transform.scale(clock_img, (int(clock_img.get_width() * scale), int(clock_img.get_height() * scale)))
minute_img = pygame.transform.scale(minute_img, (int(minute_img.get_width() * scale), int(minute_img.get_height() * scale)))
second_img = pygame.transform.scale(second_img, (int(second_img.get_width() * scale), int(second_img.get_height() * scale)))


W, H = clock_img.get_size() #width&height and setting them
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE) 
pygame.display.set_caption("Mickey Clock")

x, y = W // 2, H // 2 #setting senter of a clock face

def draw_hand(img, angle, x, y): #rotate
    rotated = pygame.transform.rotate(img, -angle)
    rect = rotated.get_rect(center=(x, y))
    screen.blit(rotated, rect.topleft)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    t = time.localtime()
    min_angle = t.tm_min * 6 + 60
    sec_angle = t.tm_sec * 6
    
    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))
    draw_hand(minute_img, min_angle, x, y)
    draw_hand(second_img, sec_angle, x, y)
    
    pygame.display.flip()
    pygame.time.delay(1000) 

pygame.quit()