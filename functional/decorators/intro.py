def file_type_aggregator(func_to_wrap):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        counts[file_type] = counts.get(file_type, 0) + 1 
        result = func_to_wrap(doc, file_type)

        return result, counts

    return wrapper


@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: {doc} with File Type: {file_type}"

