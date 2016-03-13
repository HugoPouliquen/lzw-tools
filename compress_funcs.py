def make_dict():
    dictionaryAsciiSize = 256
    dictionnary = {}

    # For each value return his string. chr(97) -> 'a'
    for i in range(dictionaryAsciiSize):
        # Build dictionnary
        dictionnary[chr(i)] = chr(i)
    return dictionnary, dictionaryAsciiSize


def compress(text):
    w = ''
    dictCompress, dictionaryAsciiSize = make_dict()
    compress = []
    for c in text:
        res = w + c
        if res in dictCompress:
            w = w + c
        else:
            compress.append(dictCompress[w])
            dictCompress[res] = dictionaryAsciiSize
            dictionaryAsciiSize += 1
            w = c
    return compress
