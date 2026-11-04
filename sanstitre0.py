import pygame
pygame.init()

# genrer la fenetre de jeu
pygame.display.set_caption("Pix'l")
screen = pygame.display.set_mode((1600, 900))

# variable
x = 775
y = 425
velocity_y = 0
cooldown = 300

# boucle du jeu
running = True

while running:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.display.flip()
    velocity_y += 0.3
    y += velocity_y
    if y >= 850:
        y = 850
        velocity_y = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if x < 1550:
                    x += 25
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if x > 0:
                    x -= 25
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if y == 850:
                    velocity_y = -10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if x < 1550:
                    x +=100
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if x > 0:
                    x -= 100
        
        if event.type == pygame.QUIT:
            running = False

pygame.quit()