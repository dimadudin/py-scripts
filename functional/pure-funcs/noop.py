def markdown_to_text(doc_content):
    lines = doc_content.split("\n")
    fmt_headings_lines = map(lambda s: s.lstrip('#'), lines)
    full_fmt_lines = map(remove_asteriks_from_words, fmt_headings_lines)
    return "\n".join(full_fmt_lines)


def remove_asteriks_from_words(line):
    words = line.split()
    fmt_words = map(lambda s: s.strip('*'), words)
    if line.startswith("* "):
        return "*" + " ".join(fmt_words)
    else:
        return " ".join(fmt_words)
