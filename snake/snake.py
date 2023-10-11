import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 游戏设置
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# 初始化窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Snake Game")

# 初始化蛇
snake = [(5, 5)]
snake_direction = (1, 0)
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
score = 0
yellow_food_count = 0
food_color = GREEN

# 游戏循环
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # 移动蛇
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    # 限制蛇的坐标在边界内
    if new_head[0] < 0:
        new_head = (GRID_WIDTH - 1, new_head[1])
    elif new_head[0] >= GRID_WIDTH:
        new_head = (0, new_head[1])
    if new_head[1] < 0:
        new_head = (new_head[0], GRID_HEIGHT - 1)
    elif new_head[1] >= GRID_HEIGHT:
        new_head = (new_head[0], 0)

    # 判断是否吃到食物
    if new_head == food:
        if yellow_food_count == 5:
            score += 10  # 黄色食物加10分
            yellow_food_count = 0  # 重置计数
        else:
            score += 5
            yellow_food_count += 1

        # 随机生成下一个食物的颜色
        if yellow_food_count == 5:
            food_color = YELLOW
        else:
            food_color = GREEN

        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        # 判断游戏结束条件，撞到自己就结束游戏
        if new_head in snake:
            running = False
        else:
            # 移动蛇身体，删除最后一节尾巴
            snake.pop()

    # 更新蛇头
    snake.insert(0, new_head)

    # 绘制背景
    screen.fill(BLACK)

    # 绘制蛇
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # 绘制食物
    pygame.draw.rect(screen, food_color, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # 显示得分
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # 更新显示
    pygame.display.flip()

    # 控制游戏速度
    clock.tick(10)

# 游戏结束，弹出消息框提示
pygame.quit()
score_message = f"游戏结束！得分: {score}\n是否重新开始游戏？"
if pygame.display.get_init():
    response = pygame.display.prompt(score_message)
    if response == 1:
        pygame.quit()
        sys.exit()
    else:
        # 重新开始游戏
        snake = [(5, 5)]
        snake_direction = (1, 0)
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        score = 0
        yellow_food_count = 0
        food_color = GREEN
        running = True