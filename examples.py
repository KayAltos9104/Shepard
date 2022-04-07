import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mass Effect 6: Проект Неман")
pygame.display.set_icon(pygame.image.load("Tali_icon.bmp"))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()

pygame.draw.rect(SURFACE, WHITE, (10, 10, 50, 100))
pygame.draw.rect(SURFACE, BLUE, (10, 250, 50, 100), 3)

pygame.display.update()

cycle_is_going = True

while cycle_is_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(30)


