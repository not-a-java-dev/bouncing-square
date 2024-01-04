import pygame
import random
def main():
    array_c = [
        (255,0,0),
        (0,255,0),
        (0,0,255),
        (255,0,255),
        (255,255,0),
        (0,255,255)
    ]
    color = random.choice(array_c)
    mx = -2 # X movement
    my = 2 # Y movement
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Hello, Pygame!")
    clock = pygame.time.Clock()
    bounds = (screen.get_width(), screen.get_height())
    run = True
    rectangle = pygame.Rect((screen.get_width()/2,screen.get_height() / 2),(50,50))
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        clock.tick(60)
        rectangle.x += mx
        rectangle.y += my
        pygame.display.flip()
        #screen.fill((0,0,0))
        pygame.draw.rect(screen,color, rectangle)
        if (rectangle.left < 0 or rectangle.right > (bounds[0])): # Collision from the sides!
            mx = -mx
            print("bing")
            color = random.choice(array_c)
        if (rectangle.top < 0 or rectangle.bottom > (bounds[1])): # Collision from the tops!
            my = -my
            print("bong")
            color = random.choice(array_c)
if __name__ == "__main__":
    main()