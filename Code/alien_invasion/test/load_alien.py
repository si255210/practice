import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置显示器的宽度和高度
width, height = 800, 600

# 创建显示器窗口
screen = pygame.display.set_mode((width, height))

# 设置窗口标题
pygame.display.set_caption("Pygame Image Display")

# 加载图片
ship = pygame.image.load("images/ship.bmp")
# 获取图片的矩形对象
ship_rect = ship.get_rect()
# 加载背景图片
background_pic = pygame.image.load('images/pexels.jpg')
# 把上面的surface类转换成屏幕大小
background = pygame.transform.scale(background_pic, (width, height))
background_rect = background.get_rect()
# 设置图片在窗口中的位置
ship_rect.centerx = background_rect.centerx
ship_rect.bottom = background_rect.bottom

bullet_group = []

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_rect.left > 0:
        ship_rect.x -= 1
    if keys[pygame.K_RIGHT] and ship_rect.right < width:
        ship_rect.x += 1
    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(ship_rect.centerx - 2, ship_rect.top, 4, 10)
        bullet_group.append(bullet)


    # 将图片绘制到屏幕上
    screen.blit(background_pic, background_rect)
    screen.blit(ship, ship_rect)

    # 更新显示
    pygame.display.flip()


