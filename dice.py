import pygame
import random

pygame.init()

screen=pygame.display.set_mode((900,700))

pygame.display.set_caption("Dice Roller")

button=pygame.Rect(300,280,220,60)
reset_button=pygame.Rect(300,380,220,60)

font=pygame.font.Font(None,36)
font=pygame.font.Font(None,45)

history=[]



dice_images = [
    pygame.transform.scale(pygame.image.load("dice1.jpg"), (90, 90)),
    pygame.transform.scale(pygame.image.load("dice2.jpg"), (90, 90)),
    pygame.transform.scale(pygame.image.load("dice3.jpg"), (90,90)),
    pygame.transform.scale(pygame.image.load("dice4.jpg"), (90, 90)),
    pygame.transform.scale(pygame.image.load("dice5.jpg"), (90,90)),
    pygame.transform.scale(pygame.image.load("dice6.jpg"), (90,90))
]

roll_sound= pygame.mixer.Sound("dice_roll.wav")
current_dice=dice_images[0]
current_dice2=dice_images[0]
roll_start=0
running=True
roll_count=0
number=1
number2=1
total=0
highest=0
lowest=0
average=0
totalsss=[]

while running:
    
    for event in pygame.event.get():
 
        if event.type==pygame.QUIT:
            running=False
    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                number=random.randint(1,6)
                current_dice=dice_images[number-1]
        
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=event.pos

            if button.collidepoint(mouse_pos):
                
                number=random.randint(1,6)
                number2=random.randint(1,6)
                current_dice=dice_images[number-1]
                current_dice2=dice_images[number2-1]
                roll_start=pygame.time.get_ticks()
                roll_sound.play()
                roll_count+=1
                total=number+number2
                
                history.append(f"{number}+{number2} ={total}")

                totalsss.append(total)

                highest=max(totalsss)
                lowest=min(totalsss)
                average=sum(totalsss)/len(totalsss)
                

            if reset_button.collidepoint(mouse_pos):
                roll_count=0
                highest=0
                lowest=0
                average=0
                number=1
                number2=1
                history.clear()

                current_dice=dice_images[0]
                current_dice2=dice_images[0]



# fill background with white colour
    screen.fill((255,255,255))
    
    mouse_pos=pygame.mouse.get_pos()

    # hover effect

    if button.collidepoint(mouse_pos):
        button_color=(0,255,0)

    else:
        button_color=(0,0,255)
# paste the image on screen
    
    screen.blit(current_dice,(280,150))
    screen.blit(current_dice2,(480,150))


    pygame.draw.rect(screen,button_color,button)
    text=font.render("ROLL DICE",True,(255,255,255))
    screen.blit(text,(340,297))

    pygame.draw.rect(screen,(255,0,0),reset_button)
    reset_text=font.render("RESET button",True,(255,255,255))
    screen.blit(reset_text,(310,400))

    roll_text=font.render(f"ROLL COUNT: {roll_count}",True,(255,0,0))
    screen.blit(roll_text,(20,20))

    current_text=font.render(f"C1:{number}",True,(0,255,10))
    screen.blit(current_text,(10,300))

    current_text2=font.render(f"C2:{number2}",True,(0,255,10))
    screen.blit(current_text2,(200,300))
    
    total_text=font.render(f"total:{total}",True,(255,0,255))
    screen.blit(total_text,(700,500))

    history_title=font.render("History",True,(0,0,255))
    screen.blit(history_title,(20,380))
    
    y=420
    for item in history:
        text=font.render(item,True,(0,0,0))
        screen.blit(text,(20,y))
        y+=30

    highest_text=font.render(f"Highest:{highest}",True,(255,0,0))
    screen.blit(highest_text,(340,20))

    lowest_text=font.render(f"lowest:{lowest}",True,(255,50,80))
    screen.blit(lowest_text,(520,20))

    average_text=font.render(f"average:{average}",True,(100,100,100))
    screen.blit(average_text,(700,20))



    pygame.display.update()
    

pygame.quit()