from utils.file_manager import output
from utils.file_manager import inputcontent
from os.path import splitext


def make_list():
    listAsciiSize = 255
    listAscii = []
    for i in range(listAsciiSize):
        listAscii.insert(i, i.to_bytes(2, 'big'))
    return listAscii, listAsciiSize


def uncompress(compressed):
    listAscii, listAsciiSize = make_list()
    uncompressed = []

    w = compressed[1]
    compressed.remove(compressed[0])
    compressed.remove(compressed[0])

    for byte in compressed:
        if byte in listAscii:
            entry = byte
        elif (int.from_bytes(byte, byteorder='big')) == listAsciiSize:
            entry = w + w  # ERREUR
        else:
            raise ValueError('Bad compressed for: %s' % byte)
        print(w)
        uncompressed.append(chr(int.from_bytes(entry, byteorder='big')))

        listAscii.insert(listAsciiSize, w + byte)
        listAsciiSize += 1
        w = entry
    #print(uncompressed)


def file_uncompressed(path):
    f = open(path, "rb")
    content = []
    for i in range(20):
        content.insert(i, f.read(2))
    uncompress(content)
    f.close()

    # filename, file_extension = splitext(path)
    # original_file = output(uncompressed, filename + '.txt')
    # return original_file
