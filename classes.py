import pygame

class Ball:
    def __init__(self, pos=[0,0], velocity=[10,10], r=50, color=(0, 0, 255)):
        self.pos = pos
        self.velocity = velocity
        self.r = r
        self.color = color
    
    def update(self, deltaTime):
        self.pos[0] += self.velocity[0] * deltaTime
        self.pos[1] += self.velocity[1] * deltaTime

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, tuple(self.pos), self.r)


class Player(Ball):
    def __init__(self):
        super().__init__(pos=[100,100], velocity=[50,50], r=25, color=(255, 255, 0))

    def update(self, deltaTime):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.velocity[0] * deltaTime
        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.velocity[0] * deltaTime
        
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.velocity[1] * deltaTime
        if keys[pygame.K_UP]:
            self.pos[1] -= self.velocity[1] * deltaTime


if __name__ == "__main__":
    pygame.init()
    S_WIDTH = 600
    S_HEIGHT = 500

    screen = pygame.display.set_mode([S_WIDTH, S_HEIGHT])

    clock = pygame.time.Clock()

    ball = Ball()
    ballB = Ball(pos=[S_WIDTH/2, S_HEIGHT/2], velocity=[20,-20])

    player = Player()

    running = True
    while running:
        dt = clock.tick()/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        ball.update(dt)
        ballB.update(dt)

        player.update(dt)

        screen.fill((225, 225, 225))

        ball.draw(screen)
        ballB.draw(screen)
        player.draw(screen)

        pygame.display.update()
    pygame.quit()