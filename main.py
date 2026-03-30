import pygame
import sys
from actions import Action

#Work in Progress
def main():
    print("Rock-Paper-Scissors Game")
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Rock-Paper-Scissors Game")
    clock = pygame.time.Clock()
    running = True
    dt = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
    pygame.quit()

if __name__ == "__main__":
    main()
