def remove_invalid_lines(document):
    return "\n".join(filter(lambda l: not (l.startswith('-')), document.split("\n")))
