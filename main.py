from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import*
from PPlay.keyboard import*
from draw import *
from scrolling import *
from asteroid_movement import *
import random

random.seed()

DIFFICULTY = 1
GAME_STATE = 0 
"""
Controla em que estágio o jogo se encontra:
0 - Menu Inicial
1 - Transição
2 - Jogo
3 - Finalização do jogo (Pontuação)
"""

"""
!!!!
Quando, dentro de uma função, você modifica alguma variável
que foi criada aqui no main, antes do GAMELOOP, 
por exemplo: "asteroids[i] = asteroid" OU "GAME_STATE = 2"
a função tem que estar aqui no main e
tem que escrever "global variável" no início.
!!!
"""

# Window
0
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
background_roll_speed = 60

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

# Text Story Panel
text1="ATENÇÃO: O planeta Terra foi invadido! A"
text2="Organização PROVA está atacando os humanos."
text3="SUA MISSÃO: Vencer a corrida de conhecimento e,"
text4="assim, salvar o mundo!"
text5="Você terá somente uma aliada, a Math, uma"
text6="astronauta com dons matemáticos."
text7="BOA SORTE!"


# Nave Personagem
ship_math = Sprite("assets\\ship_math.png", 1)
ship_math.x = 0
ship_math.y = window_height*2/4 - ship_math.height/2 - 30
# Velocidade da nave 
ship_math.speed = 5

# Nave Alienígena 1
ship_alien_1 = Sprite("assets\\ship_alien.png", 1)
ship_alien_1.x = 0
ship_alien_1.y = window_height*3/4 - ship_alien_1.height/2 - 30
# Velocidade da nave alien 1
ship_alien_1.speed = 3
#guess é a variável que indica se a pergunta foi respondida de forma correta ou não,e por ela a velocidade das naves inimigas são modificadas
guess=2 #depois tem que escrever a parte do código em que ela vai ser apresentada 
if guess==1:
    ship_alien_1.speed = ship_alien_1.speed * 0,5
elif guess==0:
    ship_alien_1.speed = ship_alien_1.speed * 2

# Nave Alienígena 2
ship_alien_2 = Sprite("assets\\ship_alien.png", 1)
ship_alien_2.x = 0
ship_alien_2.y = window_height/4 - ship_alien_2.height/2 - 30
# Velocidade da nave alien 2
ship_alien_2.speed = 3
if guess==1:
    ship_alien_2.speed = ship_alien_2.speed * 0,5
elif guess ==0:
    ship_alien_2.speed = ship_alien_2.speed * 2

# Painel De Pontos
score_panel = Sprite("assets\\score_panel.png")
score_panel.x = window_width/2 - score_panel.width/2
score_panel.y = window_height - score_panel.height

# Botões de Resposta
asw1 = Sprite("assets\\asw.png")
tinyspace= (((window_width/2 - score_panel.width/2)/2) - asw1.width)/2
asw1.x = tinyspace
asw1.y = window_height - score_panel.height
asw2 = Sprite("assets\\asw.png")
asw2.x = (3*tinyspace) + (asw2.width)
asw2.y = window_height - score_panel.height
asw3 = Sprite("assets\\asw.png")
asw3.x = (5*tinyspace) + (2*asw3.width) + (score_panel.width)
asw3.y = window_height - score_panel.height
asw4 = Sprite("assets\\asw.png")
asw4.x = (7*tinyspace) + (3*asw3.width) + (score_panel.width)
asw4.y = window_height - score_panel.height

# Imagem do Asteróide
asteroid_image = "assets\\asteroid.png"
# Velocidade do Asteróide
asteroid_speed = 70
# Tamanho do asteróide
asteroid_length = 15
# Lista de asteróides
asteroids = []

# Operador da Equação: (Para escrever na tela depois)
operator = ""
operand_1 = 0
operand_2 = 0
result = 0


def create_equation():
    """
    Função que cria as equações randomicamente
    """

    global operator
    global operand_1
    global operand_2
    global result   
    
    # escolha aleatória dos operandos
    num1 = random.randint(0,99)
    num2 = random.randint(1,99)
    operand_1 = str(num1)
    operand_2 = str(num2)

    # escolha aleatória do operador
    equation = random.randint(0, 3)
    """
    0 -> Adição / 1 -> Subtração / 2 -> Divisão / 3 -> Multiplicação
    """

    if equation == 0:
        operator = "+"
        res=num1+num2
    elif equation == 1: 
        operator = "-"
        res=num1-num2
    elif equation == 2:
        operator = "÷"
        res=num1/num2
    elif equation == 3:
        operator = "x"
        res=num1*num2


    return (operand_1+operator+operand_2) 


def spawn_asteroid():
    """
    Gera a lista de asteróides e de equações
    """
    global asteroids
    global equations 

    # Cria a lista de asteroides vazia (só com zeros)
    asteroids = [0 for _ in range(asteroid_length)]
    # Cria a lista de equações vazia 
    equations = [0 for _ in range (asteroid_length)]

    # for i percorre cada elemento da lista
    for i in range(asteroid_length):
        # Cria o Sprite do asteroide
        asteroid = Sprite(asteroid_image)
        # Cria a equação que vai estar no asteroide 
        current_equation = create_equation()
        # Define a posição dos asteroides
        asteroid.set_position(window_width + (800 * i)/DIFFICULTY, ship_math.y)
        # Define a direção do movimento, no caso esquerda
        asteroid.direction = -1  # -1 = esquerda
        # Defina se o asteroide ta aparecendo ou não (0-> Não existe \ 1 -> Existe)
        asteroid.exist = 1
        # Coloca o asteroide recém criado na lista
        asteroids[i] = asteroid
        # Coloca a equação recém criada na lista
        equations[i] = current_equation


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
    #Text Story Panel draw
    window.draw_text(str(text1), 370, 170, size=23, color=(173, 216, 230), font_name="Ariel", bold= False, italic= False)
    window.draw_text(str(text2), 370, 195, size=23, color=(173, 216, 230), font_name="Ariel", bold= False, italic= False)
    window.draw_text(str(text3), 370, 225, size=23, color=(173, 216, 230), font_name="Ariel", bold= False, italic= False)
    window.draw_text(str(text4), 370, 250, size=23, color=(173, 216, 230), font_name="Ariel", bold= False, italic= False)
    window.draw_text(str(text5), 370, 280, size=23, color=(173, 216, 230), font_name="Ariel", bold= False, italic= False)
    window.draw_text(str(text6), 370, 305, size=23, color=(173, 216, 230), font_name="Ariel", bold= False, italic= False)
    window.draw_text(str(text7), 500, 335, size=23, color=(173, 216, 230), font_name="Ariel", bold= False, italic= False)

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

        #velocidades das naves
        ship_math.x=ship_math.x + ship_math.speed*(window.delta_time())
        ship_alien_1.x=ship_alien_1.x + ship_alien_1.speed*(window.delta_time())
        ship_alien_2.x=ship_alien_2.x + ship_alien_2.speed*(window.delta_time())

        draw(ship_math, ship_alien_1, ship_alien_2, score_panel, asw1, asw2, asw3, asw4, asteroids, asteroid_length, equations, window)

        exit_race()

    # Atualizo a Janela
    window.update()
