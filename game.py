import pygame



#  START OF EVERYTHING

pygame.init()

def displayConfig():
    pygame.display.init()

    # Open a window on the screen
    screen_width=700
    screen_height=400
    screen = pygame.display.set_mode([screen_width, screen_height])
    size =  pygame.display.get_surface()

    pygame.display.update()
    pygame.display.set_caption('Halluf')

    #logo = pygame.image.load('')
    #pygame.display.set_icon(logo)

    return size
    
def colors():
    black = pygame.Color(0,0,0)
    red = pygame.Color(255,0,0)
    white = pygame.Color(255,255,255)
    green = pygame.Color(0,255,0)
    blue = pygame.Color(0,0,255)
    violet= pygame.Color(255,0,255)

    return red, white, blue, violet, green, black

def closeSys():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                assert
    return


displayConfig()
colors()

pygame.quit()
