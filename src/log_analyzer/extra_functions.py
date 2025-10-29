def messages_analysis(fragment):
    messages_map = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for line in fragment:
        parts = line.strip().split(';')
        level = parts[2].strip().upper()
        if level in messages_map:
            messages_map[level] += 1
        else:
            messages_map[level] = 1


    print(messages_map)
    return messages_map