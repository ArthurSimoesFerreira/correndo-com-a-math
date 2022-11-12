def draw(ship_math, ship_alien_1, ship_alien_2, score_panel, asteroids, asteroid_length):

    # Desenhar a nave da MATH
    ship_math.draw()
    # Desenhar os dois ALIENS
    ship_alien_1.draw()
    ship_alien_2.draw()
    # Desenhar o painel de pontos
    score_panel.draw()

    # Percorre a lista de asteroides
    for i in range(asteroid_length):
        # Caso o asteroide esteja vivo
        if asteroids[i].exist != 0:
            # Desenha ele
            asteroids[i].draw()