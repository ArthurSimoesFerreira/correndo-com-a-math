#código menu

#-----imports------#
from PPlay.window import*
from PPlay.sprite import*
from transition import*

# ------ window ------ #
window=Window(929,650)
width_window = window.width 
height_window = window.height
window.set_title("menu")
window.set_background_color((0, 0, 0))
background = Sprite("background_menu_jogofinal.jpg", 1)
background.x=0
background.y=0
mouse = Window.get_mouse()
keyboard = Window.get_keyboard()

# ------ buttons ------ #
start= Sprite("start.png",1)
width_start=260
height_start=125
start.x = ((width_window)/2 - (width_start)/2)
start.y = ((height_window)/2 + (height_start * 3/2))

# ----- story panel ----- #
width_panel= 570
height_panel= 365
panel = Sprite("storypanel.png",1)
panel.x= ((width_window)/2 - (width_panel)/2)
panel.y= ((height_window)/2 - (height_panel)*2/3)

while True:
    # ------------------- #
    background.draw()
    panel.draw()
    start.draw()

    # ----- start ------ #
    if mouse.is_over_object (start) and mouse.is_button_pressed(1) :
        transition()



    # -------------------- #
    if (keyboard.key_pressed("ESC")):
            break 

    window.update()