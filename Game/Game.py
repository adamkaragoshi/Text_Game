def game_state(health, is_alive):
    if health <= 0:
        quit("Game Over. No more health")

    elif not is_alive:
        quit("Game Over. Pitfall")

    else:
        None
