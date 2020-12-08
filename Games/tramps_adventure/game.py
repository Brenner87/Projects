import pygame

def main():
    def drawWindow():
        # global animCount
        win.blit(bg, (0, 0))
        if tramp.animCount + 1 >= frames:
            tramp.animCount = 0
        tramp.draw(win)
        for bullet in tramp.bullets:
            bullet.draw(win)
        pygame.display.update()

    frames = 30
    field = {'x': 500, 'y': 500}
    border = 5
    x = 50
    y = 424
    speed = 5
    imagesFolder = 'tramp_images'

    pygame.init()

    win = pygame.display.set_mode((field['x'], field['y']))
    pygame.display.set_caption('Cubes Game')
    clock = pygame.time.Clock()
    bg = pygame.image.load('{}/pygame_bg.jpg'.format(imagesFolder))
    tramp = player(x, y, speed)
    run = True
    while run:
        clock.tick(frames)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in tramp.bullets:
            if bullet.x < field['x'] and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                tramp.bullets.pop(tramp.bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:
            tramp.fire()
        if keys[pygame.K_LEFT] and tramp.x > border:
            tramp.moveLeft()
        elif keys[pygame.K_RIGHT] and tramp.x < field['x'] - tramp.width - border:
            tramp.moveRight()
        else:
            tramp.standStil()
        if not tramp.isJump:
            if keys[pygame.K_SPACE]:
                tramp.isJump = True
        else:
            tramp.jump()
        drawWindow()
    pygame.quit()


class player():
    def __init__(self, x, y, speed):
        imagesFolder = 'tramp_images'
        trampImgNum=6
        self.animCount=0
        self.width = 60
        self.height = 71
        self.x = x
        self.y = y
        self.speed = speed
        self.isJump= False
        self.jumpCount=10
        self.jumpLim=10
        self.left = False
        self.right = False
        self.facing = 1
        self.lastMove = 'right'
        self.bullets = []
        self.playerStand = pygame.image.load('{}/pygame_idle.png'.format(imagesFolder))
        self.walkRight = [pygame.image.load('{}/pygame_right_{}.png'.format(imagesFolder, str(i)))
                     for i in range(1, trampImgNum + 1)]

        self.walkLeft = [pygame.image.load('{}/pygame_left_{}.png'.format(imagesFolder, str(i)))
                    for i in range(1, trampImgNum + 1)]

    def moveLeft(self):
        self.left = True
        self.right = False
        self.x -= self.speed
        self.facing = -1

    def moveRight(self):
        self.left = False
        self.right = True
        self.x += self.speed
        self.facing = 1

    def standStil(self):
        self.left = False
        self.right = False
        self.animCount = 0

    def jump(self):
        if self.jumpCount >= -1*self.jumpLim:
            if self.jumpCount < 0:
                self.y+=(self.jumpCount**2)/2
            else:
                self.y-=(self.jumpCount**2)/2
            self.jumpCount-=1
        else:
            self.isJump = False
            self.jumpCount = self.jumpLim

    def fire(self):
        if len(self.bullets) < 5:
            self.bullets.append(snariad(round(self.x+self.width //2),
                                        round(self.y + self.height // 2),
                                        self.facing))

    def draw(self, win):
        self.win = win
        if self.left:
            self.win.blit(self.walkLeft[self.animCount // 5], (self.x, self.y))
            self.animCount += 1
        elif self.right:
            self.win.blit(self.walkRight[self.animCount // 5], (self.x, self.y))
            self.animCount += 1
        else:
            self.win.blit(self.playerStand, (self.x, self.y))




class snariad():
    def __init__(self, x, y, facing, radius = 5, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * self.facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

if __name__ =='__main__':
    main()