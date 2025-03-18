import pygame

pygame.init()

w, h = 500, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Moving Ball")

white = (255, 255, 255)
red = (255, 0, 0)

rad = 25
x, y = w // 2, h // 2

speed = 20
clock = pygame.time.Clock()

run = True
while run:
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), rad)
    pygame.display.flip()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - rad - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + rad + speed <= h:
        y += speed
    if keys[pygame.K_LEFT] and x - rad - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + rad + speed <= w:
        x += speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(30)

pygame.quit()