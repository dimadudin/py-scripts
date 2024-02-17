def categorize_file(filename):
    categories = {
        '.txt':'Text',
        '.docx':'Document',
        '.py':'Code',
    }
    get_category = lambda ext: categories.get(ext, 'Unknown')

    return get_category(filename[filename.rfind(".") :])

