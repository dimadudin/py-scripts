def word_count_aggregator():
    count = 0
    def aggregator(doc: str):
        nonlocal count
        count += len(doc.split())
        return count
    return aggregator
