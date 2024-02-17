def count_names(list_of_lists, target_name):
    cnt = 0
    for l in list_of_lists:
        for f in l:
            if target_name == f:
                cnt += 1
    return cnt
