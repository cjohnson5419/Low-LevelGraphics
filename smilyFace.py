import pygame, math

def drawStuff(background):

    #Smile Draw
    smilePoints = (
        (150, 300),
        (250, 370),
        (450, 370),
        (530, 300)
        )
    pygame.draw.lines(background, (0, 0, 0), False, smilePoints, 3)
    
    #Tongue Draw
    tonguePoints = (
        (208, 342),
        (208, 445),
        (300, 442),
        (333, 371)
        )
    pygame.draw.lines(background, (0, 0, 0,), False, tonguePoints, 3)
    pygame.draw.line(background, (0, 0, 0), (256, 372), (253, 419), 3)
    
    #Nose
    nosePoints = (
        (318, 205),
        (321, 273),
        (383, 305)
        )
    pygame.draw.lines(background, (0, 0, 0,), False, nosePoints, 3)
    
    #Eyes
    pygame.draw.circle(background, (0, 0, 0), (200, 150), 45)
    pygame.draw.circle(background, (0, 0, 0), (450, 150), 45)

    



    

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Drawing commands")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    drawStuff(background)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
        screen.blit(background, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()