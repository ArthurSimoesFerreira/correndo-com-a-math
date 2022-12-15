def asteroid_movement(difficulty, window, asteroids, asteroid_speed, asteroid_length):
    """
    Realiza a movimentação de cada asteroide
    """

    # Calcula a nova posição da matriz de inimigos
    new_position_x = asteroid_speed * -1 * window.delta_time() * difficulty

    # Percorre toda a lista de astroides
    for element in range(asteroid_length):
        # Caso a posição esteja preenchida, isto é, o asteroide
        # ainda esteja vivo, efetua as ações em seguida
        # Move o asteroide para sua nova posição
        asteroids[element].move_x(new_position_x)