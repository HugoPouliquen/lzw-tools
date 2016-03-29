def byteList():
    """
    Purpose: Build a byte list of 256 entries, to match the ASCII table
    Description: Convert each value, from 0 to 256, to Byte
    Param: None
    Return: A list and its size
    """
    list_ascii_size = 256
    list_ascii = []
    for i in range(list_ascii_size):
        list_ascii.insert(i, (i).to_bytes(2, 'big'))
    return list_ascii, list_ascii_size
