import pygame
pygame.init()

# genrer la fenetre de jeu
pygame.display.set_caption("Pix'l")
screen = pygame.display.set_mode((1600, 900))

# variable
x = 775
y = 425
enemy_x = 50
enemy_y = 50
enemy_speed = 2
enemy_speed_y = 2
velocity_y = 0

# boucle du jeu
running = True

while running:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (enemy_x, enemy_y, 50, 50))
    enemy_x += enemy_speed
    if enemy_x >=1550:
        enemy_speed = -2
    if enemy_x <= 0:
        enemy_speed = 2
    enemy_y += enemy_speed_y
    if enemy_y >=850:
            enemy_speed_y = -2
    if enemy_y <= 0:
            enemy_speed_y = 2
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.display.flip()
    velocity_y += 0.5
    y += velocity_y
    if y >= 850:
        y = 850
        velocity_y = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if x < 1550:
                    x += 15
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if x > 50:
                    x -= 15
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if y == 850:
                    velocity_y = -10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if y < 850:
                    y += 15
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
