def filter_messages(messages):
    filtered_messages = []
    removed_count = []
    for msg in messages:
        words = msg.split()
        filtered_words = []
        counter = 0
        for word in words:
            if word == "dang":
                counter += 1
            else:
                filtered_words.append(word)
        filtered_message = " ".join(filtered_words)
        filtered_messages.append(filtered_message)
        removed_count.append(counter)
    return filtered_messages, removed_count
