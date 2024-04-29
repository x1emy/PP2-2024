import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Red Circle")

done = False
x = 400
y = 300
x_change = 0
y_change = 0
move_amount = 20  # изменения позиции при нажатии клавиши
time=pygame.time.Clock()
fps=20
def player(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

while not done:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_change = move_amount
            if event.key == pygame.K_LEFT:
                x_change = -move_amount
            if event.key == pygame.K_DOWN:
                y_change = move_amount
            if event.key == pygame.K_UP:
                y_change = -move_amount
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0

    x += x_change
    y += y_change
    
    # Проверка на выход за границы экрана
    if x < 25:          
        x = 25
    elif x > 775:  
        x = 775 
    if y < 25:         
        y = 25
    elif y > 575:  
        y = 575

    player(x, y)
    pygame.display.update()
    time.tick(fps)
