def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        arg_list = []
        for arg in args:
            arg_list.append(convert_md_to_txt(arg))

        for key, val in kwargs.items():
            kwargs[key] = convert_md_to_txt(val)

        return func(*arg_list, **kwargs)

    return wrapper


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    fmt_lines = map(lambda line: line.lstrip("# "), lines)
    return "\n".join(fmt_lines)




# Don't edit below this line


@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""First: {first_doc}
Second: {second_doc}
"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""Title: {title}
Body: {body}
Conclusion: {conclusion}
"""

