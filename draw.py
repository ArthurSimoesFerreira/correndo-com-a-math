def draw(ship_math, ship_alien_1, ship_alien_2, score_panel, asw1, asw2, asw3, asw4, asteroids, asteroid_length, equations, window):

    # Desenhar a nave da MATH
    ship_math.draw()
    # Desenhar os dois ALIENS
    ship_alien_1.draw()
    ship_alien_2.draw()
    # Desenhar o painel de pontos
    score_panel.draw()
    # Desenhar os botões de resposta
    asw1.draw()
    asw2.draw()
    asw3.draw()
    asw4.draw()

    # Percorre a lista de asteroides
    for i in range(asteroid_length):
        # Caso o asteroide esteja vivo
        if asteroids[i].exist != 0:
            # Desenha ele
            asteroids[i].draw()
            # Desenhar as contas nos asteroide
            window.draw_text(str(equations[i]), (asteroids[i].x + 40), (asteroids[i].y + 65), size=40, color=(255, 255, 255), font_name="Ariel", bold= False, italic= False)
    

    