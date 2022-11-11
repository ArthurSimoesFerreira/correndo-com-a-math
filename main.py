from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import*
from PPlay.keyboard import*
from draw import *
from scrolling import *

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

# Asteróide
asteroid = Sprite("assets\\asteroid.png")


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

    # ESC para fechar o jogo
    if (keyboard.key_pressed("ESC")):
        exit()

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

        draw(ship_math, ship_alien_1, ship_alien_2, asteroid, score_panel)

        exit_race()

    # Atualizo a Janela
    window.update()
