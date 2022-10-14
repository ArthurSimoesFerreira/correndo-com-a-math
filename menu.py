#código menu

#-----imports------#
from PPlay.window import*
from PPlay.sprite import*
from transition import*

# ------ window ------ #
window=Window(1100,650)
width_window = window.width 
height_window = window.height
window.set_title("menu")
window.set_background_color((0, 0, 0))
background = Sprite("background_menu_jogofinal.png", 1)
background.x=0
background.y=0
mouse = Window.get_mouse()
keyboard = Window.get_keyboard()

# ------ buttons ------ #
start= Sprite("start.png",1)
start.x = 180
start.y = 180

# ----- story panel ----- #
tam_panelx= 100
tam_panely= 119
velx = 0
vely = 0
panel = Sprite("storypanel.png",1)
panel.x= 0
panel.y= 0

while True:
    # ------------------- #
    background.set_background_color((0,0,0))
    background.draw()
    panel.draw()
    start.draw()

    # ----- start ------ #
    if mouse.is_over_object (start) and mouse.is_button_pressed(1) :
        transition()



    # -------------------- #
    if (keyboard.key_pressed("ESC")):
            break 