import pygame
pygame.init()

S_WIDTH = 600
S_HEIGHT = 500

screen = pygame.display.set_mode([S_WIDTH, S_HEIGHT])

clock = pygame.time.Clock()

dx = 5 # <- Displacement in x direction
dy = 2

x = S_WIDTH/2
y = S_HEIGHT/2

r = 50

running = True
while running:
    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((225, 225, 225))

    pygame.draw.circle(screen, (0, 0, 255), (x, y), r)

    x += dx * dt # The same as x = x + dx
    y += dy * dt

    pygame.display.update()

pygame.quit()