def count_enemies(enemy_names):
    enemy_list = {}
    for enemy in enemy_names:
        if (enemy in enemy_list):
            enemy_list[enemy] += 1
        else:
            enemy_list[enemy] = 1
    return enemy_list
