import pygame
import random
import tkinter.messagebox as msgbox

# 設定視窗變數
BG_COLOR = (139, 62, 47)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 640
HEIGHT = 480
FPS = 60


pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ball')  # 設定視窗標題


# 球球的變數
r = 50
circle_x = random.randint(80, 550)
circle_y = random.randint(80, 150)
speed_x = random.choice([3, -3])
speed_y = random.choice([3, -3])

# 長方形的變數
button_x = 200
button_y = 470
button_length = 150
button_speed = 10

# 計分表變數
font = pygame.font.Font("words//微軟正黑體.ttf", 36)
score = 0
life = 3

# 遊戲規則介紹
msgbox.showinfo("Ready", "Start to play ball !\nYou have three life, if your don't have any life, the game will be over.")
print(f"Start, you have {life} life.")

run = True
clock = pygame.time.Clock()
while run:  # 讓畫面停留
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 按X後才關閉
            print("Quit")
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # 案ESC也是關閉
                print("Quit")
                run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 滑鼠左右鍵讓物體移動
            #print(event.button)
            if event.button == 1:
                #print('left')
                button_x -= button_speed
            else:
                #print('right')
                button_x += button_speed

    keys = pygame.key.get_pressed() # 透過鍵盤操控底下那條線的方式
    if keys[pygame.K_LEFT]:
        button_x -= button_speed
    if keys[pygame.K_RIGHT]:
        button_x += button_speed



    win.fill((255, 165, 0))  # 設定背景顏色

    # 球球碰壁的判斷式
    circle = pygame.draw.circle(win, (0, 255, 0), (circle_x, circle_y), r)
    #print(circle.bottom)
    if circle.top > (HEIGHT-2*r) or circle.top == 0:
        speed_y = -speed_y
        if circle.top > (HEIGHT-2*r):
            life -= 1
            speed_x -= 2
            speed_y -= 2
            print(f"Life:{life}")
    if circle.left > (WIDTH-2*r) or circle.left == 0:
        speed_x = -speed_x
    circle_x += speed_x
    circle_y += speed_y



    # 底下線的判斷式
    button = pygame.draw.line(win, (255, 100, 130), (button_x, button_y), (button_x+button_length, button_y), 20)  # 直線(視窗, 顏色, 頭的位置, 尾的位置, 邊框厚度)
    if button_x <= 0:
        button_x = 0
    elif button_x+button_length >= WIDTH:
        button_x = WIDTH-button_length


    # 球球與底下線的互動
    button_top = button.y
    button_bottom = button.y + button.width
    button_left = button.x
    button_right = button.x + button.width

    circle_top = circle_y - r
    circle_bottom = circle_y + r
    circle_left = circle_x - r
    circle_right = circle_x + r
    if circle_bottom > button_top and \
       circle_bottom < button_bottom and \
       circle_left < button_right and \
       circle_right > button_left:
        speed_y = -speed_y
        score += 1
        print(f"Score:{score}")


    # 計分表秀出來
    text_Score = font.render(f'score：{score}', True, (255, 255, 255))
    win.blit(text_Score, ((WIDTH/2)-80, 30))
    text_Life = font.render(f'Life：{life}', True, (255, 255, 255))
    win.blit(text_Life,(WIDTH-120, HEIGHT-50))

    # 遊戲規則
    if life == 0:
        msgbox.showinfo("Game Over", f"  Game over !\nYou get {score} points.")
        print("End")
        run = False

    pygame.display.update()


pygame.quit()














