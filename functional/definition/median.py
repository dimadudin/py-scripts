def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    middle_ind = len(font_sizes) // 2
    sorted_sizes = sorted(font_sizes) 
    if len(font_sizes) % 2 != 0:
        median = sorted_sizes[middle_ind]
    else:
        median = (sorted_sizes[middle_ind] + sorted_sizes[middle_ind - 1]) / 2 
    return median
