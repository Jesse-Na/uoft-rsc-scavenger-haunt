import math
import os
import random
import pygame

# constants
WALL_THICKNESS = 32
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
NUM_ENEMIES = 5
NUM_COLLECTIBLES = 3
FRAMES_PER_SPRITE = 3
FRAMES_PER_SECOND = 60
PLAYER_MOVE_SPEED = 100  # pixels per second
ENEMY_MOVE_SPEED = 100  # pixels per second
STARTING_POWER = 1.0  # starting power
STARTING_BATTERY = 100

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scavenger Haunt")
clock = pygame.time.Clock()
running = True
game_over = False
dt = 0

player_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
player_is_right = True
enemies = []  # list of tuples (enemy_pos, enemy_direction)
collectibles = []
power = STARTING_POWER
battery = STARTING_BATTERY
font = pygame.font.SysFont("Comic Sans MS", 36)

wall_img = pygame.image.load(os.path.join('images/wall.png')).convert()
wall_img = pygame.transform.scale_by(wall_img, 2)
floor_img = pygame.image.load(os.path.join('images/floor.png')).convert()
gift_img = pygame.image.load(os.path.join(
    'images/gift-box.png')).convert_alpha()
battery_img = pygame.image.load(os.path.join(
    'images/battery.png')).convert_alpha()
battery_img = pygame.transform.scale_by(battery_img, 4)
enemy_imgs = [pygame.image.load(os.path.join(
    f'images/boo-{i}.png')).convert_alpha() for i in range(1, 6)]
enemy_img_index = 0
player_imgs = [pygame.image.load(os.path.join(
    f'images/bow-{i}.png')).convert_alpha() for i in range(1, 5)]
player_img_index = 0
torch_img = pygame.image.load(os.path.join('images/torch.png')).convert_alpha()
torches = [pygame.transform.scale_by(torch_img, i) for i in range(1, 5)]


def draw_bg():
    screen.fill((0, 0, 0))  # black background to start
    screen.blit(floor_img, (0, 0))


def draw_walls():
    screen.blit(wall_img, (0, 0))  # left wall
    screen.blit(wall_img, (SCREEN_WIDTH - WALL_THICKNESS, 0))  # right wall
    screen.blit(pygame.transform.rotate(wall_img, 90), (0, 0))  # top wall
    screen.blit(pygame.transform.rotate(wall_img, 90),
                (0, SCREEN_HEIGHT - WALL_THICKNESS))  # bottom wall


def spawn_enemies():
    # spawn enemies at random positions with random directions
    for i in range(NUM_ENEMIES):
        enemy_pos = pygame.Vector2(
            random.randint(WALL_THICKNESS, SCREEN_WIDTH - WALL_THICKNESS),
            random.randint(WALL_THICKNESS, SCREEN_HEIGHT - WALL_THICKNESS)
        )
        enemy_dir = pygame.Vector2(
            random.uniform(-1, 1), random.uniform(-1, 1))
        enemies.append((enemy_pos, enemy_dir))


def spawn_collectibles():
    for i in range(NUM_COLLECTIBLES):
        collectible_pos = pygame.Vector2(
            random.randint(WALL_THICKNESS, SCREEN_WIDTH - WALL_THICKNESS),
            random.randint(WALL_THICKNESS, SCREEN_HEIGHT - WALL_THICKNESS)
        )
        collectibles.append(collectible_pos)


def draw_enemies():
    global enemy_img_index

    # shuffle through enemy images to create animated movement
    enemy_img_index = enemy_img_index + (FRAMES_PER_SPRITE / FRAMES_PER_SECOND)
    if enemy_img_index >= len(enemy_imgs):
        enemy_img_index = 0

    for i in range(len(enemies)):
        enemy_pos, _ = enemies[i]
        enemy_img = enemy_imgs[math.floor(
            enemy_img_index + i) % len(enemy_imgs)]

        screen.blit(enemy_img, (enemy_pos.x - enemy_img.get_width() /
                    2, enemy_pos.y - enemy_img.get_height() / 2))


def draw_collectibles():
    for collectible_pos in collectibles:
        screen.blit(gift_img, (collectible_pos.x - gift_img.get_width() / 2,
                               collectible_pos.y - gift_img.get_height() / 2))


def draw_player():
    global player_img_index

    # shuffle through player images to create animated movement
    player_img_index = player_img_index + \
        (FRAMES_PER_SPRITE / FRAMES_PER_SECOND)
    if player_img_index >= len(player_imgs):
        player_img_index = 0

    player_img = player_imgs[math.floor(player_img_index)]

    screen.blit(player_img, (player_pos.x - player_img.get_width() /
                2, player_pos.y - player_img.get_height() / 2))


def draw_battery():
    screen.blit(battery_img, (10, SCREEN_HEIGHT -
                battery_img.get_height() - 10))

    pygame.draw.rect(screen, (0, 255, 0), (34, SCREEN_HEIGHT - battery_img.get_height() + 2,
                     (battery_img.get_width() - 48) * (battery / 100), 32))


def check_wall_collision(pos):
    sprite_width = 32
    sprite_height = 32
    flag = False
    if pos.x < WALL_THICKNESS + sprite_width / 2:  # left wall
        pos.x = WALL_THICKNESS + sprite_width / 2
        flag = True
    if pos.x > SCREEN_WIDTH - WALL_THICKNESS - sprite_width / 2:  # right wall
        pos.x = SCREEN_WIDTH - WALL_THICKNESS - sprite_width / 2
        flag = True
    if pos.y < WALL_THICKNESS + sprite_height / 2:  # top wall
        pos.y = WALL_THICKNESS + sprite_height / 2
        flag = True
    if pos.y > SCREEN_HEIGHT - WALL_THICKNESS - sprite_height / 2:  # bottom wall
        pos.y = SCREEN_HEIGHT - WALL_THICKNESS - sprite_height / 2
        flag = True
    return flag


def check_enemy_collisions():
    for enemy_pos, _ in enemies:
        player_img = player_imgs[math.floor(player_img_index)]
        if player_pos.distance_to(enemy_pos) < math.sqrt((player_img.get_width() / 2)**2 + (player_img.get_height() / 2)**2):
            return True

    return False


def check_collectible_collisions():
    global battery, game_over

    for collectible_pos in collectibles:
        if player_pos.distance_to(collectible_pos) < 30:
            battery += 50
            if battery > 100:
                battery = 100
            collectibles.remove(collectible_pos)

    if len(collectibles) == 0:
        game_over = True


def move_enemies():
    for i in range(len(enemies)):
        enemy_pos, direction = enemies[i]
        enemy_pos.x += direction.x * ENEMY_MOVE_SPEED * dt
        enemy_pos.y += direction.y * ENEMY_MOVE_SPEED * dt

        if check_wall_collision(enemy_pos):
            # create a new direction vector
            new_dir = pygame.Vector2(
                random.uniform(-1, 1), random.uniform(-1, 1))
            enemies[i] = (enemy_pos, new_dir)


def move_player():
    global game_over, player_is_right, player_img

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= PLAYER_MOVE_SPEED * dt
    if keys[pygame.K_s]:
        player_pos.y += PLAYER_MOVE_SPEED * dt
    if keys[pygame.K_a]:
        if player_is_right:  # make player face left
            player_is_right = False
            for i in range(len(player_imgs)):
                player_imgs[i] = pygame.transform.flip(
                    player_imgs[i], True, False)
        player_pos.x -= PLAYER_MOVE_SPEED * dt
    if keys[pygame.K_d]:
        if not player_is_right:  # make player face right
            player_is_right = True
            for i in range(len(player_imgs)):
                player_imgs[i] = pygame.transform.flip(
                    player_imgs[i], True, False)
        player_pos.x += PLAYER_MOVE_SPEED * dt

    check_wall_collision(player_pos)
    if check_enemy_collisions():
        game_over = True

    check_collectible_collisions()


fog = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
fog.fill((0, 0, 0, 255))


def adjust_torch():
    global power, battery

    if battery > 0:
        battery -= power**2 * dt  # battery drains over time
    else:
        power -= dt
        if power < 0:
            power = 0

    if power > STARTING_POWER:
        power -= dt / 2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_f] and battery > 0:
        power += 1
        if power > len(torches) - 1:
            power = len(torches) - 1


def draw_fog():
    global fog

    torch = torches[math.ceil(power)]
    fog.blit(torch, (player_pos.x - torch.get_width() /
             2, player_pos.y - torch.get_height() / 2))
    # fog is on top of the screen, we want what is underneath to show
    screen.blit(fog, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    fog.fill((0, 0, 0, 255))


spawn_enemies()
spawn_collectibles()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over:  # stay on the game over screen until user closes
        if len(collectibles) == 0:
            text = font.render("You Win!", True, (0, 255, 0))
            draw_bg()
            draw_walls()
            draw_player()
            draw_enemies()
        else:
            # black out the screen
            power = 0
            draw_fog()
            text = font.render("Game Over!", True, (255, 0, 0))
        # centers the text on the screen
        screen.blit(text, text.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))

        pygame.display.flip()
        dt = clock.tick(FRAMES_PER_SECOND) / 1000  # limits FPS to 60
        continue

    draw_bg()
    draw_walls()

    move_player()  # have to move before drawing or else collision looks weird
    move_enemies()
    adjust_torch()

    draw_player()
    draw_enemies()
    draw_collectibles()
    draw_fog()
    draw_battery()

    pygame.display.flip()  # display your drawing to the screen
    dt = clock.tick(FRAMES_PER_SECOND) / 1000  # limits FPS to 60

pygame.quit()
