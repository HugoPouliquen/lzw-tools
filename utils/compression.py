from os.path import splitext
from utils.file_manager import output
from utils.file_manager import input_content
from utils.make_list import byte_list


def compress(bytes_text):
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
    content = input_content(path)
    filename, file_extension = splitext(path)
    compressed = compress(content)
    lzw_file = output(compressed, filename + '.lzw')
    return lzw_file
