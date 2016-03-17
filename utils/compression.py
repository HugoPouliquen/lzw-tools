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
            compressed.append(dictCompress[w])
            dictCompress[res] = dictionaryAsciiSize
            dictionaryAsciiSize += 1
            w = c
    return compressed
