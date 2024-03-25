from tkinter import NW
import pygame

pygame.init()
screen=pygame.display.set_mode((1280,722),pygame.RESIZABLE)
pygame.display.set_caption("Moldanazar player")
done=False

img=pygame.image.load("img/moldanazar1.jpeg")
def_img=(50,50)
next=pygame.image.load("img/next.png")
next=pygame.transform.scale(next,def_img)
previous=pygame.image.load("img/previous.png")
previous=pygame.transform.scale(previous,def_img)
stop=pygame.image.load("img/stop.png")
stop=pygame.transform.scale(stop,(60,60))
play=pygame.image.load("img/play.png")
play=pygame.transform.scale(play,(45,45))

font=pygame.font.SysFont("Apple Chancery.ttf",32)
text=font.render("",True,(0,128,0))

song=['music/mahabbatym.mp3','music/ozin_gana.mp3','music/alystama.mp3']
current_song_index=0
k_right_count=0
k_left_count=0
pygame.mixer.music.load(song[current_song_index])
pygame.mixer.music.play()
paused=True


while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                k_right_count+=1
                current_song_index=(current_song_index+1)%len(song)
                pygame.mixer.music.load(song[current_song_index])
                pygame.mixer.music.play()
            if event.key==pygame.K_LEFT:
                k_left_count+=1
                current_song_index=(current_song_index-1)%len(song)
                pygame.mixer.music.load(song[current_song_index])
                pygame.mixer.music.play()
            if event.key==pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.pause()
                    paused=False
                else:
                    pygame.mixer.music.unpause()
                    paused=True
            
    screen.blit(img,(0,0))
    screen.blit(next,(210,600))
    
    screen.blit(stop,(145,595))
    screen.blit(previous,(89,600))
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    
    pygame.display.update()
    #screen.blit(next,(263,600))
    #screen.blit(stop,(194,595))
    #screen.blit(previous,(137,600))