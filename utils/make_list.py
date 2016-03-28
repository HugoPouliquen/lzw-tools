def byte_list():
    """
    Purpose: Build bytes list of 256 entries. Corresponds to the ASCII table
    Description: Between 0-256, each value (1, 2, 3, ...) transform in byte value
    Param: Nothing
    Return: list and size of list
    """
    listAsciiSize = 256
    listAscii = []
    for i in range(listAsciiSize):
        listAscii.insert(i, (i).to_bytes(2, 'big'))
    return listAscii, listAsciiSize
