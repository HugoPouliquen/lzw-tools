def byteList():
    """
    Purpose: Build bytes list of 256 entries. Corresponds to the ASCII table
    Description: Between 0-256, each value (1, 2, 3, ...) transform in byte value
    Param: Nothing
    Return: list and size of list
    """
    list_ascii_size = 256
    list_ascii = []
    for i in range(list_ascii_size):
        list_ascii.insert(i, (i).to_bytes(2, 'big'))
    return list_ascii, list_ascii_size
