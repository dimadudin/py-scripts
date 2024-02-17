def count_nested_levels(nested_documents, target_document_id, level=1):
    if target_document_id in nested_documents:
        return level
    for _, value in nested_documents.items():
        res = count_nested_levels(value, target_document_id, level + 1)
        if res != -1:
            return res
    return -1
