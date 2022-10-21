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
background = Sprite("assets\\background_menu.png", 1)
background.x=0
background.y=0
mouse = Window.get_mouse()
keyboard = Window.get_keyboard()

# ------ buttons ------ #
start= Sprite("assets\\button_start.png",1)
start.x = ((width_window)/2 - (start.width)/2)
start.y = ((height_window)/2 + (start.height * 3/1.8))

# ----- story panel ----- #
story_window = Sprite("assets\\window_story.png",1)
story_window.x= ((width_window)/2 - (story_window.width)/2)
story_window.y= ((height_window)/2 - (story_window.height)*2/3)

while True:
    # ------------------- #
    background.draw()
    story_window.draw()
    start.draw()

    # ----- start ------ #
    if mouse.is_over_object (start) and mouse.is_button_pressed(1) :
        transition()



    # -------------------- #
    if (keyboard.key_pressed("ESC")):
            break 

    window.update()