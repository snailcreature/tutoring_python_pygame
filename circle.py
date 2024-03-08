import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

clock = pygame.time.Clock()

dx = 5
dy = 2

x = 0
y = 0

running = True
while running:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((225, 225, 225))

    pygame.draw.circle(screen, (0, 0, 255), (x, y), 75)

    x += dx # The same as x = x + dx
    y += dy

    pygame.display.update()

pygame.quit()