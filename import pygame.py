# Créé par nelson3, le 25/11/2026 en Python 3.7
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
jump_force = -9

on_ground = False

# Position d'arrivé
player_end = (1525, 240, 50, 100)

# Dash : pas encore debloque
dash_unlocked = False
dash_available = False

dash_speed = 15
dash_duration = 10
is_dashing = False
dash_direction = 0
dash_timer = 0

    # Mur
wall = pygame.Rect(1550, 250, 75, 600),

# Terrain
ground = pygame.Rect(0, 850, 1600, 50)

platforms = [
    # Parcours principal
    pygame.Rect(130, 770, 110, 15),
    pygame.Rect(300, 690, 90, 15),
    pygame.Rect(130, 610, 100, 15),

    # Grande branche
    pygame.Rect(420, 500, 190, 18),

    # Petit détour facultatif
    pygame.Rect(900, 650, 100, 15),
    pygame.Rect(1080, 560, 90, 15),

    # Dernière ascension
    pygame.Rect(920, 430, 110, 15),
    pygame.Rect(1250, 350, 100, 15),
    pygame.Rect(1515, 240, 110, 15)
]

#caméra
camera_x = 0
world_width = 3200

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

    # Arrivé
    player_rect = pygame.Rect(x, y, 50, 50)

    if player_rect.colliderect(player_end):
        print("Niveau terminé")

    #mouvement de la caméra
    target_camera = max(0, x - 1550)

    camera_x += (target_camera - camera_x) * 0.1

    # Sol + plateformes
    all_platforms = [ground] + platforms

    for platform in all_platforms:

        if (velocity_y >= 0
            and previous_bottom <= platform.top
            and player_rect.bottom >= platform.top
            and player_rect.right >= platform.left
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
        screen_rect = platform.move(-camera_x, 0)
        pygame.draw.rect(screen, (100, 160, 100), screen_rect)

    pygame.draw.rect(screen, (0, 255, 0), player_end)

    # Dessin du personnage
    pygame.draw.rect(screen, (255, 0, 0),
    (x - camera_x, y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
