def pad_len(string, length):
    return length - len(string.encode('GBK')) + len(string)