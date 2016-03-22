from utils.file_manager import output
from utils.file_manager import inputcontent
from os.path import splitext

# For each value return his string. chr(97) -> 'a'
def make_dict():
    dictionaryAsciiSize = 256
    dictionnary = {}
    for i in range(dictionaryAsciiSize):
        dictionnary[chr(i)] = chr(i)
    return dictionnary, dictionaryAsciiSize


def compress(text):
    w = fstr = ''
    dictCompress, dictionaryAsciiSize = make_dict()
    compressed = []
    for c in text:
        res = w + c
        if res in dictCompress:
            w = w + c
        else:
            if type(dictCompress[w]) == bytes:
                compressed.append(dictCompress[w])
            else:
                compressed.append(dictCompress[w].encode())
            dictCompress[res] = (dictionaryAsciiSize).to_bytes(2, 'little')
            dictionaryAsciiSize += 1
            w = c
    return compressed


def file_compression(path):
    content = inputcontent(path)
    compressed = compress(content)
    filename, file_extension = splitext(path)
    lzw_file = output(compressed, filename + '.lzw')
    return lzw_file
