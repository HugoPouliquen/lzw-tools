from os.path import splitext
from utils.file_manager import output
from utils.file_manager import input_content
from utils.make_list import byte_list


def compress(bytes_text):
    """
    Purpose: Compress byte text
    Description: to each value in byte text convert byte on two byte and then
    if value of result of concat in the list (alors) pas
    Param: text in byte to compress
    Return: filename
    """
    w = bytes()
    listAscii, listAsciiSize = byte_list()
    compressed = []
    for c in bytes_text:
        c = c.to_bytes(2, 'big')
        wc = w + c
        if wc in listAscii:
            w = wc
        else:
            listAscii.insert(listAsciiSize, wc)
            compressed.append(listAscii.index(w).to_bytes(2, 'big'))
            listAsciiSize += 1
            w = c
    return compressed


def file_compression(path):
    """
    Purpose: Manage function for compress in file
    Description: Extract base content, extract basename of file, compress and
    put in file with lzw extension
    Param: path for file to compress
    Return: LZW file name
    """
    content = input_content(path)
    filename, file_extension = splitext(path)
    compressed = compress(content)
    lzw_file = output(compressed, filename + '.lzw')
    return lzw_file
