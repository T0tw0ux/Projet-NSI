
import pygame
pygame.init()

# Fenetre
pygame.display.set_caption("Pix'l")
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()

# Variables du personnage
x = 775
y = 800

velocity_x = 0
velocity_y = 0

speed = 5
gravity = 0.3
jump_force = -10

on_ground = False

# Dash : pas encore debloque
dash_unlocked = False
dash_available = False

dash_speed = 15
dash_duration = 10
is_dashing = False
dash_direction = 0
dash_timer = 0

# Terrain
ground = pygame.Rect(0, 850, 1600, 50)

platforms = [
    pygame.Rect(450, 720, 140, 20),
    pygame.Rect(700, 620, 130, 20),
    pygame.Rect(1000, 680, 140, 20),
    pygame.Rect(1250, 550, 130, 20)
]

# Boucle du jeu
running = True

while running:

    screen.fill((20, 35, 25))

    # Evenements
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Saut
            if event.key == pygame.K_SPACE:
                if on_ground and not is_dashing:
                    velocity_y = jump_force
                    on_ground = False

            # Dash droite
            if event.key == pygame.K_e:
                if dash_unlocked and dash_available and not is_dashing:
                    is_dashing = True
                    dash_direction = 1
                    dash_timer = dash_duration
                    dash_available = False

            # Dash gauche
            if event.key == pygame.K_a:
                if dash_unlocked and dash_available and not is_dashing:
                    is_dashing = True
                    dash_direction = -1
                    dash_timer = dash_duration
                    dash_available = False

    # Touches maintenues
    keys = pygame.key.get_pressed()

    if is_dashing:
        velocity_x = dash_speed * dash_direction
        dash_timer -= 1

        if dash_timer <= 0:
            is_dashing = False

    else:
        if keys[pygame.K_d]:
            velocity_x = speed
        elif keys[pygame.K_q]:
            velocity_x = -speed
        else:
            velocity_x = 0

    # Deplacement horizontal
    x += velocity_x
    x = max(0, min(x, 1550))

    # Gravite et collisions
    previous_bottom = y + 50
    was_on_ground = on_ground

    if is_dashing:
        velocity_y = 0
    else:
        y += velocity_y
        velocity_y += gravity

    on_ground = False

    player_rect = pygame.Rect(x, y, 50, 50)

    # Sol + plateformes
    all_platforms = [ground] + platforms

    for platform in all_platforms:

        if (velocity_y >= 0
            and previous_bottom <= platform.top
            and player_rect.bottom >= platform.top
            and player_rect.right > platform.left
            and player_rect.left < platform.right):

            y = platform.top - 50
            velocity_y = 0
            on_ground = True

            # Recharge du dash a l'atterrissage
            if not was_on_ground and dash_unlocked:
                dash_available = True

            break

    # Dessin du terrain
    pygame.draw.rect(screen, (70, 110, 65), ground)

    for platform in platforms:
        pygame.draw.rect(screen, (100, 150, 80), platform)

    # Dessin du personnage
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
