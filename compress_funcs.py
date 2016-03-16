from os.path import basename
from os.path import splitext

def make_dict():
    dictionaryAsciiSize = 256
    dictionnary = {}

    # For each value return his string. chr(97) -> 'a'
    for i in range(dictionaryAsciiSize):
        # Build dictionnary
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
            compressed.append(dictCompress[w])
            dictCompress[res] = dictionaryAsciiSize
            dictionaryAsciiSize += 1
            w = c
    return compressed


# def byte_transformed(text):
#     bList = []
#     for item in text:
#         bList.append(bytes(str(item), 'UTF-8'))
#     print(bList)
#     return bList

def filename_extracted(filename):
    base = basename(filename)
    name = splitext(base)[0]
    return name

def input(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    compressed = compress(content)
    filename = output(compressed, filename_extracted(filename) + '.lzw')
    # bList = byte_transformed(compressed)
    # filename = output(bList, 'compressed.lzw')
    return filename


def output(text, filename):
    f = open(filename, 'w')
    for item in text:
        f.write(str(item))
        f.write(' ')
    f.close()
    return filename

    # fb = open(filename, 'wb')
    # for item in bList:
    #     fb.write(item)
    #     fb.write(bytes(' ', 'UTF-8'))
    # fb.close()
    # return filename
