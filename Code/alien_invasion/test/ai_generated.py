import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 设置窗口大小
screen_width = 800
screen_height = 600

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 初始化窗口
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("外星人入侵")

# 设置字体
font = pygame.font.SysFont(None, 48)

# 定义玩家飞船
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - 20 - player_height
player_speed = 5

# 定义子弹
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# 定义外星人
alien_width = 50
alien_height = 50
alien_speed = 2
alien_spawn_delay = 60
aliens = []

# 初始化游戏状态
score = 0
lives = 3
game_over = False

# 生成外星人
def spawn_alien():
    alien = {
        'rect': pygame.Rect(random.randint(0, screen_width - alien_width), 0, alien_width, alien_height),
        'speed': alien_speed
    }
    aliens.append(alien)

# 游戏主循环
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            bullet = pygame.Rect(player_x + player_width // 2 - bullet_width // 2, player_y, bullet_width, bullet_height)
            bullets.append(bullet)

    # 移动子弹
    for bullet in bullets:
        bullet.y -= bullet_speed

    # 移动外星人
    for alien in aliens:
        alien['rect'].y += alien['speed']

    # 检测子弹与外星人的碰撞
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien['rect']):
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 1

    # 检测外星人是否到达底部或与玩家飞船碰撞
    for alien in aliens[:]:
        if alien['rect'].bottom >= screen_height or alien['rect'].colliderect(player_x, player_y, player_width, player_height):
            aliens.remove(alien)
            lives -= 1

    # 生成新的外星人
    alien_spawn_delay -= 1
    if alien_spawn_delay <= 0:
        spawn_alien()
        alien_spawn_delay = 60

    # 检测游戏结束条件
    if lives <= 0:
        game_over = True

    # 绘制背景
    screen.fill(black)

    # 绘制玩家飞船
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

    # 绘制子弹
    for bullet in bullets:
        pygame.draw.rect(screen, white, bullet)

    # 绘制外星人
    for alien in aliens:
        pygame.draw.rect(screen, red, alien['rect'])

    # 绘制分数和生命
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    lives_text = font.render(f"Lives: {lives}", True, white)
    screen.blit(lives_text, (screen_width - 150, 10))

    # 绘制游戏结束文本
    if game_over:
        game_over_text = font.render("Game Over", True, white)
        screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 24))

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)
