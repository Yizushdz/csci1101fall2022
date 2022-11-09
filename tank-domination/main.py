import pygame

pygame.init()

# Create game screen.
monitor_display = (800, 600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

game_tank_svg = pygame.image.load("tank.svg")
game_tank_sprite = pygame.transform.scale(game_tank_svg, (75, 75))

game_characteristics = {
    "sky": {
        "color": (135, 206, 235)
    },
    "Grass": {
        "color": (0, 255, 0), 
        "Position": {
            "y": 0.8 * monitor_display[1]
        }
    },
    "Player": {
        "Position": {
            "x": 0.2 * monitor_display[0] 
        },
        "hp": 1
    },
    "cpu": {
    "Position": {
        "x": 0.8 * monitor_display[0] - game_tank_sprite.get_width()
    },
    "hp": 1
    }
}

# Game logic.
game_running_flag = True

while game_running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running_flag = False

    if not game_running_flag:
        pygame.quit()
        break

    key_pressed = pygame.key.get_pressed()
    position_delta = 0
    if key_pressed[pygame.K_LEFT]:
        position_delta = -1
    elif key_pressed[pygame.K_RIGHT]:
        position_delta = 1

    if 0 <= game_characteristics["Player"]["Position"]["x"] + position_delta and game_characteristics["Player"]["Position"]["x"] + position_delta + game_tank_sprite.get_width() <= game_characteristics["cpu"]["Position"]["x"]:
        game_characteristics["Player"]["Position"]["x"] += position_delta

    # game graphics
    game_display.fill(game_characteristics["sky"]["color"])
    pygame.draw.rect(game_display, game_characteristics["Grass"]["color"], pygame.Rect(0, game_characteristics["Grass"]["Position"]["y"], monitor_display[0], monitor_display[1] - game_characteristics["Grass"]["Position"]["y"]))

    game_tank_sprite_player = game_tank_sprite
    game_display.blit(game_tank_sprite_player, (game_characteristics["Player"]["Position"]["x"], game_characteristics["Grass"]["Position"]["y"] - game_tank_sprite_player.get_height())) 

    game_tank_sprite_cpu = pygame.transform.flip(game_tank_sprite, True, False)
    game_display.blit(game_tank_sprite_cpu, (game_characteristics["cpu"]["Position"]["x"], game_characteristics["Grass"]["Position"]["y"] - game_tank_sprite_cpu.get_height()))

    # Render game frame by frame
    pygame.display.update()

    system_clock.tick(30)