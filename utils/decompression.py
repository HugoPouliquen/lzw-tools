from os.path import splitext
from os.path import getsize
from utils.make_list import byteList


def decompress(compressed, path):
    """
    Purpose: Decompress file
    Description: Read the file to decompress, remove the fist couple of byte.
    Then, decompress each byte using the ASCII list and convert it into
    2 bytes. ??? . And finally write the decompress sequence to the file.
    Param: Path of file to compress
    Return: Name of the file in param .txt (for the moment)
    """
    list_ascii, list_ascii_size = byteList()
    uncompressed = []
    i = 0
    filename, file_extension = splitext(path)
    f = open(filename + '2.txt', 'wb')
    w = compressed[0]
    compressed.remove(compressed[0])

    f.write(w)
    for byte_element in compressed:
        int_element = int.from_bytes(byte_element, byteorder='big')

        if int_element < list_ascii_size:
            entry = list_ascii[int_element]
        elif int_element == list_ascii_size:
            entry = w + w
        else:
            raise ValueError('Bad uncompressed for: %s' % byte_element)

        for byte in entry:
            if i % 2 == 1:
                f.write(byte.to_bytes(1, byteorder='big'))
            i += 1

        list_ascii.insert(list_ascii_size, w + byte_element)
        list_ascii_size += 1
        w = entry
    f.close()
    return filename + '2.txt'


def fileDecompression(path):
    """
    Purpose: Decompresse a file
    Description: Open a file in read and byte mode. Put each group of two
    byte in an array.
    Param: Path of file to decompress
    Return: Decompressed content
    file
    """
    f = open(path, "rb")
    content = []
    for i in range(int(getsize(path)/2)):
        content.insert(i, f.read(2))
    f.close()
    return decompress(content, path)
