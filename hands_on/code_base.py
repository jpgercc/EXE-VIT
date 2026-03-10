import pygame

# dontpad.com/cgzs
# https://drive.google.com/drive/folders/1r1yXUAYClB-Lzw3J9e0McVbyrQmtmyts?usp=drive_link
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            screen.fill((30, 30, 30))
      # draw/update here

pygame.quit()