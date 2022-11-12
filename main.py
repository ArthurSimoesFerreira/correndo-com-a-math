from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import*
from PPlay.keyboard import*
from draw import *
from scrolling import *
from asteroid_movement import *

DIFFICULTY = 1
GAME_STATE = 0 
"""
Controla em que estágio o jogo se encontra:
0 - Menu Inicial
1 - Transição
2 - Jogo
3 - Finalização do jogo (Pontuação)
"""

# Window
background_color = [0, 0, 0]
window = Window(1100, 650)
window_width = window.width
window_height = window.height
window.set_background_color(background_color)

# Keyboard & Mouse
keyboard = window.get_keyboard()
mouse = window.get_mouse()

# Backgrounds
background_race_1 = GameImage("assets\\background_space.png")
background_race_2 = GameImage("assets\\background_space_reversed.png")

background_race_1.x = 0
background_race_2.x = window_width

# Velocidade de rolagem
background_roll_speed = 50

background_menu = Sprite("assets\\background_menu.png", 1)
background_menu.x = window_width/2 - background_menu.width/2
background_menu.y = window_height/2 - background_menu.height/2

# Buttons
button_start = Sprite("assets\\button_start.png",1)
button_start.x = ((window_width)/2 - (button_start .width)/2)
button_start.y = ((window_height)/2 + (button_start .height * 3/1.8))

# Story Panel
story_panel = Sprite("assets\\window_story.png",1)
story_panel.x= ((window_width)/2 - (story_panel.width)/2)
story_panel.y= ((window_height)/2 - (story_panel.height)*2/3)

# Nave Personagem
ship_math = Sprite("assets\\ship_math.png", 1)
ship_math.x = 0
ship_math.y = window_height*2/4 - ship_math.height/2 - 30

# Nave Alienígena 1
ship_alien_1 = Sprite("assets\\ship_alien.png", 1)
ship_alien_1.x = 0
ship_alien_1.y = window_height*3/4 - ship_alien_1.height/2 - 30

# Nave Alienígena 2
ship_alien_2 = Sprite("assets\\ship_alien.png", 1)
ship_alien_2.x = 0
ship_alien_2.y = window_height/4 - ship_alien_2.height/2 - 30

# Painel De Pontos
score_panel = Sprite("assets\\score_panel.png")
score_panel.x = window_width/2 - score_panel.width/2
score_panel.y = window_height - score_panel.height

# Imagem do Asteróide
asteroid_image = "assets\\asteroid.png"
# Velocidade do Asteróide
asteroid_speed = 50
# Tamanho do asteróide
asteroid_length = 5
# Lista de asteróides
asteroids = []


def spawn_asteroid():
    """
    Gera a lista de asteróides
    """
    global asteroids

    # Cria a lista de asteroides vazia (só com zeros)
    asteroids = [0 for _ in range(asteroid_length)]

    # for i percorre cada elemento da lista
    for i in range(asteroid_length):
        # Cria o Sprite do asteroide
        asteroid = Sprite(asteroid_image)
        # Define a posição dos asteroides
        asteroid.set_position(window_width + (800 * i)/DIFFICULTY, ship_math.y)
        # Define a direção do movimento, no caso esquerda
        asteroid.direction = -1  # -1 = esquerda
        # Defina se o asteroide ta aparecendo ou não (0-> Não existe \ 1 -> Existe)
        asteroid.exist = 1
        # Coloca o asteroide recém criado na lista
        asteroids[i] = asteroid


def restart():
    """
    Reinicia o Jogo 
    """
    # Apaga tudo na lista de asteroides
    asteroids.clear()

    # Cria de novo todos os asteroids
    spawn_asteroid()


def exit_race():

    global GAME_STATE

    if keyboard.key_pressed("ESC"):
        GAME_STATE = 0


def menu():

    global GAME_STATE

    story_panel.draw()
    button_start.draw()

    # Apertar o botão para começar o jogo
    if mouse.is_over_object (button_start) and mouse.is_button_pressed(1) :
        GAME_STATE = 2
        restart()

    # ESC para fechar o jogo
    if (keyboard.key_pressed("ESC")):
        exit()


# GAME LOOP
while True:

    if GAME_STATE == 0:
        background_menu.draw()
        menu()


    elif GAME_STATE == 1:
        pass


    # Se não for a primeira vez, quer dizer que a partida ainda
    # está acontecendo. 
    elif GAME_STATE == 2:

        scrolling(window, background_race_1, background_race_2, background_roll_speed)

        asteroid_movement(DIFFICULTY, window, asteroids, asteroid_speed, asteroid_length)

        draw(ship_math, ship_alien_1, ship_alien_2, score_panel, asteroids, asteroid_length)

        exit_race()

    # Atualizo a Janela
    window.update()
