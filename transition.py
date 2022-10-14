from PPlay.window import*
from PPlay.sprite import*

def transition():
    #gamecode
    while True:
        window.set_background_color((0,0,0))

        if (keyboard.key_pressed("ESC")):
            break 

        window.update()