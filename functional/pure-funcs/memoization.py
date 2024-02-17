def word_count_memo(document, memos):
    if document not in memos:
        memos[document] = word_count(document)
    return memos[document], memos


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count

