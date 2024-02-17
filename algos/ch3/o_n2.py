def does_name_exist(first_names, last_names, full_name):
    for fname in first_names:
        for lname in last_names:
            if (" ".join([fname, lname]) == full_name):
                return True
    return False

