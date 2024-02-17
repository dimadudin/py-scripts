def get_most_common_enemy(enemies_dict):
    most_common_enemy = None
    max_count = float("-inf")
    for enemy_name in enemies_dict:
        enemy_count = enemies_dict[enemy_name]
        if enemy_count >= max_count:
            max_count = enemy_count
            most_common_enemy = enemy_name
    return most_common_enemy
