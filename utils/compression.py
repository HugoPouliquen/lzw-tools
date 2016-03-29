from os.path import splitext
from utils.file_manager import output
from utils.file_manager import inputContent
from utils.make_list import byteList


def compress(bytes_text):
    """
    Purpose: Compress byte text
    Description: to each value in byte text convert byte on two byte and then
    if value of result of concat in the list so if result it's in list, continue
    else you put the result in list and add value in compress array on 2 bytes
    Param: text in byte to compress
    Return: filename
    """
    w = bytes()
    list_ascii, list_ascii_size = byteList()
    compressed = []
    for c in bytes_text:
        c = c.to_bytes(2, 'big')
        wc = w + c
        if wc in list_ascii:
            w = wc
        else:
            list_ascii.insert(list_ascii_size, wc)
            compressed.append(list_ascii.index(w).to_bytes(2, 'big'))
            list_ascii_size += 1
            w = c
    return compressed


def fileCompression(path):
    """
    Purpose: Manage function for compress in file
    Description: Extract base content, extract basename of file, compress and
    put in file with lzw extension
    Param: path for file to compress
    Return: LZW file name
    """
    content = inputContent(path)
    filename, file_extension = splitext(path)
    compressed = compress(content)
    lzw_file = output(compressed, filename + '.lzw')
    return lzw_file
