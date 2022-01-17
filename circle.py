import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 400))

    RUNNING = True

    while RUNNING:
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, pygame.Color(0, 0, 255), (400, 200), 100)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False


if __name__ == "__main__":
    main()
