def scrolling(window, bg_left, bg_right, roll_speed):
    """
    Recebe dois background e a velocidade que devem rolar infinitamente
    :param bg_left: Sprite do fundo 1
    :param bg_right: Sprite do fundo 2
    :param roll_speed: Velocidade de deslocamento dos fundos
    """
     
    # Movimenta ambos os Sprites verticalmente 
    bg_left.x -= roll_speed * window.delta_time()
    bg_right.x -= roll_speed * window.delta_time()
 
    # Se a imagem da direita já tiver sido completamente exibida,
    # retorna ambas imagens às suas posições iniciais
    if bg_right.x + bg_right.width <= 0:
        bg_right.x = window.width
    if bg_left.x + bg_left.width <= 0:
        bg_left.x = window.width 
 
 
    # Renderiza as duas imagens de fundo
    bg_left.draw()
    bg_right.draw()