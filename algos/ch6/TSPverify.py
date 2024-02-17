def verify_tsp(paths, dist, actual_path):
    net_distance = 0
    for i in range(1, len(actual_path)):
        net_distance += paths[actual_path[i]][actual_path[i - 1]]
    if net_distance < dist:
        return True
    return False
