import sys, pygame, math
pygame.init()
from collections import *

size = WIDTH, HEIGHT = 1200, 800
black = 0, 0, 0
x, y = 10, 500
w, h = 40, 40
r=10
frames=30
vel=3
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

map =[
'             ',
' _ _ _ _ _ _ ',
' _ _ _ _ _ _ ',
' _ _ _ _ _ _ ',
]


def get_side_of_tuch(me_obj, obj):
    def get_degry(x, y):
        rad = math.atan2(-y, x)
        rad %= 2 * math.pi
        return math.degrees(rad)

    x = obj.rect.centerx - me_obj.rect.centerx
    y = obj.rect.centery - me_obj.rect.centery

    vect = (me_obj.rect.w / 2 + obj.rect.w / 2, me_obj.rect.h / 2 + obj.rect.h / 2)

    bottom_right = get_degry(vect[0], vect[1])
    bottom_left = get_degry(-vect[0], vect[1])
    top_right = get_degry(vect[0], -vect[1])
    top_left = get_degry(-vect[0], -vect[1])

    cur_angle = get_degry(x, y)
    print('Top left: ' +str(top_left))
    print('Current: ' + str(cur_angle))
    print('Bottom left: ' + str(bottom_left))


    if bottom_left >= cur_angle > top_left:
        return 'left'
    if top_right >= cur_angle or cur_angle > bottom_right:
        return 'right'
    if top_right < cur_angle <= top_left:
        return 'top'
    if bottom_right >= cur_angle > bottom_left:
        return 'bottom'


class Structure(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super(Structure, self).__init__()
        self.color = color
        self.create_surface(x, y, w, h)
        self.durability = 6
        self.destruct = w//self.durability, h//self.durability

    def create_surface(self, x, y, w, h):
        print('w:{}|h:{}'.format(w, h))
        self.image = pygame.Surface((w, h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def destruction(self, bullet):
        dw = self.rect.w - self.destruct[0]
        dh = self.rect.h - self.destruct[1]
        dx = self.rect.x + self.destruct[0]
        dy = self.rect.y + self.destruct[1]
        x = self.rect.x
        y = self.rect.y
        h = self.rect.h
        w = self.rect.w
        #print(self.rect.h)
        #print(dw)
        bullet.kill()
        # touch_side = get_side_of_tuch(self, bullet)
        # if touch_side == 'left' and collisions['left']:
        #     self.create_surface(dx, y, dw, h)
        # if touch_side == 'right' and collisions['right']:
        #     self.create_surface(x, y, dw, h)
        # if touch_side == 'top' and collisions['top']:
        #     self.create_surface(x, dy, w, dh)
        # if touch_side == 'bottom' and collisions['bottom']:
        #     self.create_surface(x, y, w, dh)

        if bullet.speed[0] > 0:
            self.create_surface(dx, y, dw, h)
        if bullet.speed[0] < 0:
            self.create_surface(x, y, dw, h)
        if bullet.speed[1] >0:
            self.create_surface(x, dy, w, dh)
        if bullet.speed[1] <0:
            self.create_surface(x, y, w, dh)

        if self.rect.w <= 0 or self.rect.h <= 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color, velocity, speed=[0,0]):
        super(Player, self).__init__()
        self.color = color
        self.speed = speed
        self.velocity = velocity
        self.bullets_in_use = pygame.sprite.Group()
        self.max_bullets = 1
        self.direction = [1, 0]
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.nav_keys = {'idle': [0, 0], pygame.K_RIGHT: [1, 0], pygame.K_LEFT: [-1, 0], pygame.K_UP: [0, -1],
                         pygame.K_DOWN: [0, 1]}
        self.keys_pressed = OrderedDict()
        self.keys_pressed['idle'] = [0, 0]

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, structures):
        def get_degry(x, y):
            rad=math.atan2(-y, x)
            rad %= 2*math.pi
            return math.degrees(rad)
        for i in structures:
            if pygame.sprite.collide_rect(self, i):
                side = get_side_of_tuch(self, i)

                if side == 'left':
                    self.rect.left = i.rect.right
                    return
                if side == 'right':
                    self.rect.right = i.rect.left
                    return
                if side == 'top':
                    self.rect.top = i.rect.bottom
                    return
                if side == 'bottom':
                    self.rect.bottom = i.rect.top
                    return

        xBorder = self.rect.centerx + self.direction[0] * self.rect.w / 2
        yBorder = self.rect.centery + self.direction[1] * self.rect.h / 2
        if xBorder < WIDTH and xBorder > 0:
            self.rect.x += self.speed[0]
        if yBorder < HEIGHT and yBorder > 0:
            self.rect.y += self.speed[1]
        
    def move_on_key_down(self):
        self.keys_pressed[event.key] = self.nav_keys[event.key]
        self.speed = [i * self.velocity for i in list(self.keys_pressed.items())[-1][-1]]
        self.direction = list(self.keys_pressed.items())[-1][-1]

    def move_on_key_up(self):
        if len(list(self.keys_pressed))>=1:
            self.direction = self.keys_pressed.pop(event.key)
            self.speed = [i * self.velocity for i in list(self.keys_pressed.items())[-1][-1]]
        if len(list(self.keys_pressed)) >= 2:
            self.direction = list(self.keys_pressed.items())[-1][-1]

    def fire(self, bullet):
        if self.max_bullets > len(self.bullets_in_use):
            self.bullets_in_use.add(bullet)

    def bullet_start(self):
        x = self.rect.centerx + w / 2 * self.direction[0]
        y = self.rect.centery + h / 2 * self.direction[1]
        return (x, y)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, velocity=7, speed=[0,0]):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.color = (0,255,0)
        self.speed = speed
        self.image.fill(self.color)
        self.velocity = velocity

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.x >=WIDTH or self.rect.x <=0:
            self.kill()
        if self.rect.y >=HEIGHT or self.rect.y <=0:
            self.kill()


char=Player(x, y, w, h, (255, 0, 0), vel)
structures=pygame.sprite.Group()
wall=Structure(100, 100, 60, 60, (255,200,28))
startx = 0
starty = 0
for i in map:
    for j in i:
        if j == '_':
            structures.add(Structure(startx, starty, 60, 60, (255,200,28)))
        startx +=60
    starty += 60
    startx = 0
#


game_over=False
while not game_over:
    clock.tick(frames)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key in char.nav_keys.keys():
            char.move_on_key_down()

        if event.type == pygame.KEYUP and event.key in char.nav_keys.keys():
            char.move_on_key_up()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            char.fire(Bullet(*char.bullet_start(), 7, 7, speed=[7*i for i in char.direction]))

    hits = pygame.sprite.groupcollide(structures, char.bullets_in_use, False, False)
    #if hits:
        #print(hits)
    for structure in hits:
        for bullet in hits[structure]:
            structure.destruction(bullet)
    screen.fill(black)
    char.draw(screen)
    #pygame.sprite.groupcollide()
    char.move(structures)


    for i in structures:
        i.draw(screen)

    for i in char.bullets_in_use:
        i.draw(screen)
        i.move()
    pygame.display.update()