from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4
    


def convert_format(content, from_format, to_format):
    if from_format == DocFormat.MD and to_format == DocFormat.HTML:
        return "<h1>" + content.lstrip("# ") + "</h1>"
    elif from_format == DocFormat.TXT and to_format == DocFormat.PDF:
        return "[PDF] " + content + " [PDF]"
    elif from_format == DocFormat.HTML and to_format == DocFormat.MD:
        return "# " + content.strip("</h1>")
    else:
        raise Exception("Invalid type")
