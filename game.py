from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import*
from PPlay.keyboard import*

def start_game():

    window = Window(1100,650)
    mouse = window.get_mouse()
    keyboard = window.get_keyboard()

    # Background
    backgroundMenu = Sprite("fundo_corrida.png", 1)
    backgroundMenu.x = window.width/2 - backgroundMenu.width/2

    # Nave Personagem
    navePersonagem = Sprite("nave_personagem.png", 1)
    navePersonagem.x = 0
    navePersonagem.y = window.height*2/4 - navePersonagem.height/2 - 30

    # Nave Alienígena 1
    naveAlien1 = Sprite("nave_alien.png", 1)
    naveAlien1.x = 0
    naveAlien1.y = window.height*3/4 - naveAlien1.height/2 - 30
    
    # Nave Alienígena 2
    naveAlien2 = Sprite("nave_alien.png", 1)
    naveAlien2.x = 0
    naveAlien2.y = window.height/4 - naveAlien2.height/2 - 30

    # Painel De Pontos
    painelPontos = Sprite("painel.png")
    painelPontos.x = window.width/2 - painelPontos.width/2
    painelPontos.y = window.height - painelPontos.height

    # Asteróide
    asteroide = Sprite("asteroide.png")
    asteroide.x = 800
    asteroide.y = navePersonagem.y 

    while(True):
        
        backgroundMenu.draw()
        navePersonagem.draw()
        naveAlien1.draw()
        naveAlien2.draw()
        asteroide.draw()
        painelPontos.draw()

        if keyboard.key_pressed("ESC"):
            break
        window.update()

start_game()