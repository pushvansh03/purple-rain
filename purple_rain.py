from utilities import *

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Purple Rain")

run = True
d = {}
for i in range(200) :
    d[i] = drop()

while run :

    for event in pygame.event.get() :

        if event.type == pygame.QUIT :
            run = False
        
        if event.type == pygame.KEYDOWN:
            
            if (event.key == pygame.K_UP) :
                if drop.slow_status() :
                    drop.drop_up()
                drop.drop_slow()
                 
            if (event.key == pygame.K_DOWN) :
                if drop.up_status() == False :
                    drop.drop_fast()
                if drop.up_status() :
                    drop.drop_down()
                
        if event.type == pygame.MOUSEBUTTONDOWN :
            change_color()
            
    win.fill(get_bgcolor())
    
    for i in d :
        d[i].fall()
        d[i].show(win)
        
    pygame.display.update()

