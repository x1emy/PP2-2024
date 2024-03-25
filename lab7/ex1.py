import pygame, datetime
pygame.init()

screen=pygame.display.set_mode((900,1000),pygame.RESIZABLE)
done=False
pygame.display.set_caption("Micky Mouse Watch")

icon=pygame.image.load("img/mickeyclock.jpeg")
pygame.display.set_icon(icon)
img=pygame.image.load("img/mainclock.png")
right=pygame.image.load("img/rightarm.png")
left=pygame.image.load("img/leftarm.png")

while not done:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.blit(img,(-250,-100))

    minute=datetime.datetime.now().minute
    second=datetime.datetime.now().second
    minute_angle=minute*6
    second_angle=second*6

    rotated_right=pygame.transform.rotate(right,-minute_angle)
    right_rect=rotated_right.get_rect(center=img.get_rect(center=(450,450)).center)
    screen.blit(rotated_right,right_rect)

    rotated_left=pygame.transform.rotate(left,-second_angle)
    left_rect=rotated_left.get_rect(center=img.get_rect(center=(450,450)).center)
    screen.blit(rotated_left,left_rect)

    pygame.display.update()