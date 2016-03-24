from utils.file_manager import output
from utils.file_manager import inputcontent
from os.path import splitext


# For each value return his string. chr(97) -> 'a'
def make_list():
    listAsciiSize = 256
    listAscii = []
    for i in range(listAsciiSize):
        listAscii.insert(i, i.to_bytes(2, 'big'))
    return listAscii, listAsciiSize


def compress(text):
    w = (0).to_bytes(2, 'big')
    listAscii, listAsciiSize = make_list()
    compressed = []
    for c in text:
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
    content = inputcontent(path)
    compressed = compress(content)
    filename, file_extension = splitext(path)
    lzw_file = output(compressed, filename + '.lzw')
    return lzw_file
