import copy

def add_format(default_formats, new_format):
    user_formats = copy.copy(default_formats)
    user_formats[new_format] = True
    return user_formats

def remove_format(default_formats, old_format):
    user_formats = copy.copy(default_formats)
    user_formats[old_format] = False
    return user_formats
