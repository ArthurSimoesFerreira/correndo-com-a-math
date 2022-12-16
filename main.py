from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import*
from PPlay.keyboard import*
from PPlay.sound import*
from draw import *
from scrolling import *
from asteroid_movement import *
from answer import*
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

# Fundo Preto
background_black = Sprite("assets\\black_background.png")
background_black.x = 0
background_black.y = 0

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
ship_math.speed = 3

# Nave Alienígena 1
ship_alien_1 = Sprite("assets\\ship_alien.png", 1)
ship_alien_1.x = 0
ship_alien_1.y = window_height*3/4 - ship_alien_1.height/2 - 30
# Velocidade da nave alien 1
ship_alien_1.speed = 3.01

# Nave Alienígena 2
ship_alien_2 = Sprite("assets\\ship_alien.png", 1)
ship_alien_2.x = 0
ship_alien_2.y = window_height/4 - ship_alien_2.height/2 - 30
# Velocidade da nave alien 2
ship_alien_2.speed = 3.01

# Painel De Pontos
score_panel = Sprite("assets\\score_panel.png")
score_panel.x = window_width/2 - score_panel.width/2
score_panel.y = window_height - score_panel.height

# Pontuação
ship_math.score = 0
scorex=score_panel.x + (score_panel.width/2)
scorey= window_height - score_panel.height + (score_panel.height/4)

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

# Em quais botões cada opção vai ficar
button_1_option = 0
button_2_option = 0
button_3_option = 0
button_4_option = 0

# Imagem do Asteróide
asteroid_image = "assets\\asteroid.png"
# Velocidade do Asteróide
asteroid_speed = 70
# Tamanho da lista de asteróides
asteroid_length = 10
# Lista de asteróides
asteroids = []
# Lista de equações string
equations_strings = []
# Lista de opções de respostas (A equations_options[_][4] é sempre a correta)
equations_options = []

# Linha de Chegada
finish_line = Sprite("assets\\finish_line.png")
# Posição inicial da linha de chegada
finish_line.set_position(window_width, 0)

# Imagem e texto finais
final_image = 0
final_text = 0

# O GANHADOR (1 -> Jogador   0 -> Aliens)
winner = 1

# Timer Transition
timer = 0

# Fonte
fonte = pygame.font.SysFont('ariel', 50, True, False)

# Tela
screen = window.screen

# Criação dos efeitos sonoros
transition_sound = Sound("sounds//transition_sound.ogg")


def create_equation():
    """
    Função que cria as equações randomicamente
    """  
    global equations_strings
    global equations_options

    # escolha aleatória do operador
    equation = random.randint(0, 3)
    # 0 -> Adição / 1 -> Subtração / 2 -> Divisão / 3 -> Multiplicação

    if equation == 0:
        # escolha aleatória dos operandos
        num1 = random.randint(0,50)
        num2 = random.randint(1,50)
        operand_1 = str(num1)
        operand_2 = str(num2)

        operator = "+"
        res=num1+num2
    elif equation == 1: 
        # escolha aleatória dos operandos
        num1 = random.randint(0,50)
        num2 = random.randint(1,50)
        operand_1 = str(num1)
        operand_2 = str(num2)

        operator = "-"
        res=num1-num2
    elif equation == 2:
        # escolha aleatória dos operandos
        num2 = random.randint(1,50)
        num1 = random.randint(num2,num2 + 50)
        operand_1 = str(num1)
        operand_2 = str(num2)

        operator = "÷"
        res = round(num1/num2, 2)
    elif equation == 3:
        # escolha aleatória dos operandos
        num1 = random.randint(0,50)
        num2 = random.randint(1, 50)
        operand_1 = str(num1)
        operand_2 = str(num2)

        operator = "x"
        res=num1*num2

    # Adiciona a lista [opção1, opção2, opção3(a mais perto), res] na matriz de opções
    equations_options.append(answer(num1, num2, equation, res))

    return (operand_1+operator+operand_2) 


def onscreen():
    """
    Verifica sempre se o asteroide está na tela ou não, mudando a propriedade
    E sorteia os botões de cada opção
    """

    global button_1_option
    global button_2_option
    global button_3_option
    global button_4_option

    for i in range(len(asteroids)):
        if (((asteroids[i].x > 0 - asteroids[i].width) and (asteroids[i].x < window.width)) and 
        (asteroids[i].is_onscreen == 0) and (asteroids[i].destroyed==0)):
            # Define que o asteróide entrou na tela nesse momento
            asteroids[i].is_onscreen = 1
            # Sortea a opção que vai aparecer em cada botão
            # Os whiles não deixam que uma opção seja igual a outra
            # O range está (0,3) porque iremos precisar desse número para verficar a lista de opções
            button_1_option = random.randint(0,3)

            button_2_option = random.randint(0,3)
            while (button_2_option == button_1_option):
                button_2_option = random.randint(0,3)

            button_3_option = random.randint(0,3)
            while (button_3_option == button_1_option or button_3_option == button_2_option):
                button_3_option = random.randint(0,3)

            button_4_option = random.randint(0,3)
            while (button_4_option == button_1_option or button_4_option == button_2_option or button_4_option == button_3_option):
                button_4_option = random.randint(0,3)
            
        if (((asteroids[i].x - asteroid_speed * window.delta_time() <= 0 - asteroids[i].width) or 
        (asteroids[i].x > window.width)) and (asteroids[i].is_onscreen == 1)):
            # Define que o asteróide saiu da tela nesse momento
            asteroids[i].is_onscreen = 0


def spawn_asteroid():
    """
    Gera a lista de asteróides e de equações
    """
    global asteroids
    global equations_strings 

    # Cria a lista de asteroides vazia (só com zeros)
    asteroids = [0 for _ in range(asteroid_length)]
    # Cria a lista de equações vazia 
    equations_strings = [0 for _ in range (asteroid_length)]

    # for i percorre cada elemento da lista
    for i in range(asteroid_length):
        # Cria o Sprite do asteroide
        asteroid = Sprite(asteroid_image)
        # Cria a equação que vai estar no asteroide 
        current_equation = create_equation()
        # Define a posição dos asteroides
        asteroid.set_position(window_width + (1202 * i)/DIFFICULTY, ship_math.y)
        # Define a direção do movimento, no caso esquerda
        asteroid.direction = -1  # -1 = esquerda
        # Defina se o asteroide ta aparecendo ou não (0-> Não existe \ 1 -> Existe)
        asteroid.exist = 1
        # Define se o asteroide está na tela ou não (0 -> Não está \ 1 -> Está)
        asteroid.is_onscreen = 0
        # Definir se foi destruido
        asteroid.destroyed = 0
        # Coloca o asteroide recém criado na lista
        asteroids[i] = asteroid
        # Coloca a equação recém criada na lista
        equations_strings[i] = current_equation


def finish_line_movement():
    """
    Função que move e desenha a linha de chegada
    ela também verifica de a nave chegou na linha de chegada
    """
    global finish_line
    global GAME_STATE
    global winner

    # Se o último asteróide tiver passado da nave
    if asteroids[asteroid_length - 1].x <= ship_math.x:
        # Desenhar a linha 
        finish_line.draw()
        # Mover a linha
        finish_line.move_x(asteroid_speed * -1 * window.delta_time() * DIFFICULTY)

        # Se a nave do jogador ultrapassar a linha de chegada
        if (ship_math.x + ship_math.width) > (finish_line.x + finish_line.width):
            # Ganhador é o jogador
            winner = 1
            GAME_STATE = 3
            create_final()
        # Se a nave de um dos aliens ultrapassar a linha de chegada
        elif (ship_alien_1.x + ship_alien_1.width) > (finish_line.x + finish_line.width) or (ship_alien_2.x + ship_alien_2.width) > (finish_line.x + finish_line.width):
            # Ganhador é o alien
            winner = 0
            GAME_STATE = 3
            create_final()


def show_options():
    """
    Mostro todas as opções nos botões
    """
    for i in range(len(asteroids)):
        if asteroids[i].is_onscreen == 1:
            # Escrever no botão 1
            button_1_string = f"{equations_options[i][button_1_option]}"
            grouping_button_1 = fonte.render(button_1_string, False, (255,255,255))
            text_button_1 = grouping_button_1.get_rect()
            text_button_1.center = (asw1.x + asw1.width/2, asw1.y + asw1.height/2)
            screen.blit(grouping_button_1, (asw1.x + asw1.width/2 - text_button_1.width/2 , asw1.y + asw1.height/2 - text_button_1.height/2))
            # Escrever no botão 2
            button_2_string = f"{equations_options[i][button_2_option]}"
            grouping_button_2 = fonte.render(button_2_string, False, (255,255,255))
            text_button_2 = grouping_button_2.get_rect()
            text_button_2.center = (asw2.x + asw2.width/2, asw2.y + asw2.height/2)
            screen.blit(grouping_button_2, (asw2.x + asw2.width/2 - text_button_2.width/2 , asw2.y + asw2.height/2 - text_button_2.height/2))
            # Escrever no botão 3
            button_3_string = f"{equations_options[i][button_3_option]}"
            grouping_button_3 = fonte.render(button_3_string, False, (255,255,255))
            text_button_3 = grouping_button_3.get_rect()
            text_button_3.center = (asw3.x + asw3.width/2, asw3.y + asw3.height/2)
            screen.blit(grouping_button_3, (asw3.x + asw3.width/2 - text_button_3.width/2 , asw3.y + asw3.height/2 - text_button_3.height/2))
            # Escrever no botão 4
            button_4_string = f"{equations_options[i][button_4_option]}"
            grouping_button_4 = fonte.render(button_4_string, False, (255,255,255))
            text_button_4 = grouping_button_4.get_rect()
            text_button_4.center = (asw4.x + asw4.width/2, asw4.y + asw4.height/2)
            screen.blit(grouping_button_4, (asw4.x + asw4.width/2 - text_button_4.width/2 , asw4.y + asw4.height/2 - text_button_4.height/2))

def ship_asteroid_colission():
    """
    Colisão entre nave e asteróide
    """
    for i in range(asteroid_length):
        if (asteroids[i].x + 40) <= ((ship_math.x + ship_math.width)):
            if asteroids[i].exist == 1 and asteroids[i].is_onscreen == 1:
                #aumenta a velocidade dos aliens
                ship_math.speed=ship_math.speed*0.9
                ship_alien_1.speed=ship_alien_1.speed*1.1
                ship_alien_2.speed=ship_alien_2.speed*1.1

                asteroids[i].exist = 0
                asteroids[i].is_onscreen = 0
                asteroids[i].destroyed = 1

def click():
    
    if mouse.is_over_object (asw1) and mouse.is_button_pressed(1) :
        for j in range(len(asteroids)):
            if asteroids[j].is_onscreen == 1:  
                if equations_options[j][button_1_option]== equations_options[j][3]:           
                    #soma ponto
                    ship_math.score += 1
                    #tira o asteroid
                    asteroids[j].exist = 0
                    #aumenta a velocidade da nave
                    ship_math.speed=ship_math.speed * 1.1
                    ship_alien_1.speed=ship_alien_1.speed * 0.9
                    ship_alien_2.speed=ship_alien_2.speed * 0.9
                    
                else:
                    #tira o asteroid
                    asteroids[j].exist=0
                    #aumenta a velocidade dos aliens
                    ship_math.speed=ship_math.speed*0.9
                    ship_alien_1.speed=ship_alien_1.speed*1.1
                    ship_alien_2.speed=ship_alien_2.speed*1.1

                asteroids[j].exist = 0
                asteroids[j].is_onscreen = 0
                asteroids[j].destroyed = 1
    if mouse.is_over_object (asw2) and mouse.is_button_pressed(1) :
        for j in range(len(asteroids)):
            if asteroids[j].is_onscreen==1:  
                if equations_options[j][button_2_option]== equations_options[j][3]:           
                    #soma ponto
                    ship_math.score +=1
                    #tira o asteroid
                    asteroids[j].exist=0
                    #aumenta a velocidade da nave
                    ship_math.speed=ship_math.speed*1.1
                    ship_alien_1.speed=ship_alien_1.speed*0.9
                    ship_alien_2.speed=ship_alien_2.speed*0.9
                    
                    
                else:
                    #tira o asteroid
                    asteroids[j].exist=0
                    #aumenta a velocidade dos aliens
                    ship_math.speed=ship_math.speed*0.9
                    ship_alien_1.speed=ship_alien_1.speed*1.1
                    ship_alien_2.speed=ship_alien_2.speed*1.1
                    
                asteroids[j].exist=0
                asteroids[j].is_onscreen=0
                asteroids[j].destroyed=1
                    
    if mouse.is_over_object (asw3) and mouse.is_button_pressed(1) :
        for j in range(len(asteroids)):
            if asteroids[j].is_onscreen==1:  
                if equations_options[j][button_3_option]== equations_options[j][3]:           
                    #soma ponto
                    ship_math.score +=1
                    #tira o asteroid
                    asteroids[j].exist=0
                    #aumenta a velocidade da nave
                    ship_math.speed=ship_math.speed*1.1
                    ship_alien_1.speed=ship_alien_1.speed*0.9
                    ship_alien_2.speed=ship_alien_2.speed*0.9

                    
                else:
                    #tira o asteroid
                    asteroids[j].exist=0
                    #aumenta a velocidade dos aliens
                    ship_math.speed=ship_math.speed*0.9
                    ship_alien_1.speed=ship_alien_1.speed*1.1
                    ship_alien_2.speed=ship_alien_2.speed*1.1
                    
                asteroids[j].exist=0
                asteroids[j].is_onscreen=0
                asteroids[j].destroyed=1
    if mouse.is_over_object (asw4) and mouse.is_button_pressed(1) :
        for j in range(len(asteroids)):
            if asteroids[j].is_onscreen==1:  
                if equations_options[j][button_4_option]== equations_options[j][3]:           
                    #soma ponto
                    ship_math.score +=1
                    #tira o asteroid
                    asteroids[j].exist=0
                    #aumenta a velocidade da nave
                    ship_math.speed=ship_math.speed*1.1
                    ship_alien_1.speed=ship_alien_1.speed*0.9
                    ship_alien_2.speed=ship_alien_2.speed*0.9
                    
                else:
                    #tira o asteroid
                    asteroids[j].exist=0
                    #aumenta a velocidade dos aliens
                    ship_math.speed=ship_math.speed*0.9
                    ship_alien_1.speed=ship_alien_1.speed*1.1
                    ship_alien_2.speed=ship_alien_2.speed*1.1
                    
                asteroids[j].exist=0
                asteroids[j].is_onscreen=0
                asteroids[j].destroyed=1


# Tela de transição (3, 2, 1) ==> falta botar o 3,2,1 e fazer de fato funcionar (tem algo dando errado com os sprites)
def restart():
    """
    Reinicia o Jogo 
    """
    #reinicia a contagem de pontos
    ship_math.score = 0 

    # reinicia as velocidades
    ship_math.speed = 3
    ship_alien_1.speed = 3.01
    ship_alien_2.speed = 3.01

    # reinicia as posições
    ship_math.x = 0
    ship_alien_1.x = 0
    ship_alien_2.x = 0

    # Apaga tudo na lista de asteroides
    asteroids.clear()

    # Apagar tudo na lista de equações
    equations_options.clear()
    equations_strings.clear()
    # Cria de novo todos os asteroids
    spawn_asteroid()


def transition():
    global GAME_STATE
    global timer

    window.set_background_color((0,0,0))

    transition_sound.play()

    if (timer < 30):
        if (timer>=0.0) and (timer<0.3):
            background_sprite = Sprite("assets\space_jump-0.png",1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        if (timer>=0.3) and (timer<0.6):
            background_sprite = Sprite("assets\space_jump-0.png",1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        if (timer>=0.6) and (timer<0.9):
            background_sprite = Sprite("assets\space_jump-1.png",1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=0.9) and (timer<1.2):
            background_sprite = Sprite("assets\space_jump-2.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=1.2) and (timer<1.5):
            background_sprite = Sprite("assets\space_jump-3.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=1.5) and (timer<1.8):
            background_sprite = Sprite("assets\space_jump-4.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=1.8) and (timer<2.1):
            background_sprite = Sprite("assets\space_jump-5.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=2.1) and (timer<2.4):
            background_sprite = Sprite("assets\space_jump-6.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=2.4) and (timer<2.7):
            background_sprite = Sprite("assets\space_jump-7.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=2.7) and (timer<3):
            background_sprite = Sprite("assets\space_jump-8.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=3) and (timer<3.3):
            background_sprite = Sprite("assets\space_jump-9.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=3.3) and (timer<3.6):
            background_sprite = Sprite("assets\space_jump-10.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=3.6) and (timer<3.9):
            background_sprite = Sprite("assets\space_jump-11.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=3.9) and (timer<4.2):
            background_sprite = Sprite("assets\space_jump-12.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=4.2) and (timer<4.5):
            background_sprite = Sprite("assets\space_jump-13.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=4.5) and (timer<4.8):
            background_sprite = Sprite("assets\space_jump-14.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=4.8) and (timer<5.1):
            background_sprite = Sprite("assets\space_jump-15.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=5.1) and (timer<5.4):
            background_sprite = Sprite("assets\space_jump-16.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=5.4) and (timer<5.7):
            background_sprite = Sprite("assets\space_jump-17.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=5.7) and (timer<6.0):
            background_sprite = Sprite("assets\space_jump-18.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=6.0) and (timer<6.3):
            background_sprite = Sprite("assets\space_jump-19.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=6.3) and (timer<6.6):
            background_sprite = Sprite("assets\space_jump-20.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=6.6) and (timer<6.9):
            background_sprite = Sprite("assets\space_jump-21.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=6.9) and (timer<7.2):
            background_sprite = Sprite("assets\space_jump-22.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=7.2) and (timer<7.5):
            background_sprite = Sprite("assets\space_jump-23.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=7.5) and (timer<7.8):
            background_sprite = Sprite("assets\space_jump-24.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=7.8) and (timer<8.1):
            background_sprite = Sprite("assets\space_jump-25.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=8.1) and (timer<8.4):
            background_sprite = Sprite("assets\space_jump-26.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=8.4) and (timer<8.7):
            background_sprite = Sprite("assets\space_jump-27.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=8.7) and (timer<9.0):
            background_sprite = Sprite("assets\space_jump-28.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=9) and (timer<9.3):
            background_sprite = Sprite("assets\space_jump-29.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=9.3) and (timer<9.6):
            background_sprite = Sprite("assets\space_jump-30.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=9.6) and (timer<10.2):
            background_sprite = Sprite("assets\space_jump-31.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=10.2) and (timer<10.5):
            background_sprite = Sprite("assets\space_jump-32.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=10.5) and (timer<10.8):
            background_sprite = Sprite("assets\space_jump-33.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=10.8) and (timer<11.1):
            background_sprite = Sprite("assets\space_jump-34.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=11.1) and (timer<11.4):
            background_sprite = Sprite("assets\space_jump-35.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=11.4) and (timer<11.7):
            background_sprite = Sprite("assets\space_jump-36.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=11.7) and (timer<12.0):
            background_sprite = Sprite("assets\space_jump-37.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=12) and (timer<12.3):
            background_sprite = Sprite("assets\space_jump-0.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=12.3) and (timer<12.6):
            background_sprite = Sprite("assets\space_jump-1.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=12.6) and (timer<13.2):
            background_sprite = Sprite("assets\space_jump-2.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=13.2) and (timer<13.5):
            background_sprite = Sprite("assets\space_jump-3.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=13.5) and (timer<13.8):
            background_sprite = Sprite("assets\space_jump-4.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=13.8) and (timer<14.1):
            background_sprite = Sprite("assets\space_jump-5.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=14.4) and (timer<14.7):
            background_sprite = Sprite("assets\space_jump-6.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=14.7) and (timer<15.0):
            background_sprite = Sprite("assets\space_jump-7.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=15) and (timer<15.3):
            background_sprite = Sprite("assets\space_jump-8.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=15.3) and (timer<15.6):
            background_sprite = Sprite("assets\space_jump-9.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=15.6) and (timer<16.2):
            background_sprite = Sprite("assets\space_jump-10.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=16.2) and (timer<16.5):
            background_sprite = Sprite("assets\space_jump-11.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=16.5) and (timer<16.8):
            background_sprite = Sprite("assets\space_jump-12.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=16.8) and (timer<17.1):
            background_sprite = Sprite("assets\space_jump-13.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=17.4) and (timer<17.7):
            background_sprite = Sprite("assets\space_jump-14.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=17.7) and (timer<18.0):
            background_sprite = Sprite("assets\space_jump-15.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=18) and (timer<18.3):
            background_sprite = Sprite("assets\space_jump-16.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=18.3) and (timer<18.6):
            background_sprite = Sprite("assets\space_jump-17.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=18.6) and (timer<19.2):
            background_sprite = Sprite("assets\space_jump-18.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=19.2) and (timer<19.5):
            background_sprite = Sprite("assets\space_jump-19.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=19.5) and (timer<19.8):
            background_sprite = Sprite("assets\space_jump-20.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()
        elif (timer>=19.8) and (timer<20.1):
            background_sprite = Sprite("assets\space_jump-21.png", 1)
            background_sprite.x = 0
            background_sprite.y = 0
            background_sprite.draw()

        timer += 0.04
    
    else:
        GAME_STATE = 2
        timer = 0
        restart()
            

def create_final():
    """
    Escolha da imagem final e do texto final
    """

    global final_text
    global final_image
    
    if winner == 0:
        final_text = Sprite("assets\\text_ending_bad.png")
        final_image = Sprite("assets\\photo_ending_bad.png")

    elif (winner == 1) and (ship_math.score <= 6):
        final_text = Sprite("assets\\text_ending_ok.png")
        final_image = Sprite("assets\\photo_ending_ok.png")

    elif (winner == 1) and (ship_math.score <= 9):
        final_text = Sprite("assets\\text_ending_nice.png")
        final_image = Sprite("assets\\photo_ending_nice.png")

    final_text.x = window_width/2 - final_text.width/2
    final_text.y = window_height

    final_image.x = 0
    final_image.y = 0

def show_final():
    """
    Mostrar o final
    """
    #reinicia a contagem de pontos
    ship_math.score = 0 


    if ((final_text.y + final_text.height) >= 0):
        final_text.move_y(-0.2)
    
    if ((final_text.y + final_text.height) < 0):
        GAME_STATE = 0
    
    final_image.draw()
    final_text.draw()


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
        GAME_STATE = 1

    # ESC para fechar o jogo
    if (keyboard.key_pressed("ESC")):
        exit()


# GAME LOOP
while True:

    if GAME_STATE == 0:
        background_black.draw()
        background_menu.draw()
        menu()


    elif GAME_STATE == 1:
        transition()


    # Se não for a primeira vez, quer dizer que a partida ainda
    # está acontecendo. 
    elif GAME_STATE == 2:

        scrolling(window, background_race_1, background_race_2, background_roll_speed)

        asteroid_movement(DIFFICULTY, window, asteroids, asteroid_speed, asteroid_length)
        
        #velocidades das naves
        ship_math.x=ship_math.x + ship_math.speed*(window.delta_time())
        ship_alien_1.x=ship_alien_1.x + ship_alien_1.speed*(window.delta_time())
        ship_alien_2.x=ship_alien_2.x + ship_alien_2.speed*(window.delta_time())

        finish_line_movement()
        
        onscreen()

        draw(ship_math, ship_alien_1, ship_alien_2, score_panel, asw1, asw2, asw3, asw4, asteroids, asteroid_length, equations_strings, window)

        show_options()

        ship_asteroid_colission()

        click()

        window.draw_text(str(ship_math.score), scorex, scorey, size=50, color=(173, 216, 230), font_name="Ariel", bold= False, italic= False)
        
        exit_race()


    elif GAME_STATE == 3:

        show_final()

    # Atualizo a Janela
    window.update()
