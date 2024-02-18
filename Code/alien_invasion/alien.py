import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 设置显示器的宽度和高度
width, height = 800, 600

# 创建显示器窗口
screen = pygame.display.set_mode((width, height))

# 设置窗口标题
pygame.display.set_caption("Alien Invasion")

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 定义玩家飞船
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += 5

# 定义子弹
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(BLACK)  # 修改这里为黑色
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -8

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# 定义外星人
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-50, -10)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > height:
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = random.randint(-50, -10)
            self.speed = random.randint(1, 3)

# 创建玩家飞船
player = Player()

# 创建子弹组
bullets = pygame.sprite.Group()

# 创建外星人组
aliens = pygame.sprite.Group()
for _ in range(10):
    alien = Alien()
    aliens.add(alien)

# 创建时钟对象来控制游戏循环速度
clock = pygame.time.Clock()

# 初始化得分
score = 0
font = pygame.font.Font(None, 36)

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # 按下空格键时，发射子弹
            bullet = Bullet(player.rect.centerx, player.rect.top)
            bullets.add(bullet)

    # 更新玩家飞船
    player.update()

    # 更新外星人
    aliens.update()

    # 更新子弹
    bullets.update()

    # 检测子弹与外星人的碰撞
    hits = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for hit in hits:
        # 子弹击中外星人，增加得分
        score += 1
        # 创建新的外星人
        alien = Alien()
        aliens.add(alien)

    # 检测飞船与外星人的碰撞
    if pygame.sprite.spritecollide(player, aliens, dokill=True):
        print("Player hit by alien!")
        # 处理飞船被外星人击中的逻辑，这里简化为打印信息

    # 清除屏幕
    screen.fill(WHITE)

    # 绘制玩家飞船
    screen.blit(player.image, player.rect)

    # 绘制外星人
    for alien in aliens:
        screen.blit(alien.image, alien.rect)

    # 绘制子弹
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)

    # 绘制得分
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # 更新显示
    pygame.display.flip()

    # 控制游戏循环速度
    clock.tick(30)
