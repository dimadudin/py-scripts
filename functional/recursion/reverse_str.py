def reverse_string(s):
    if not s:
        return ""
    return reverse_string(s[1:]) + s[0]
