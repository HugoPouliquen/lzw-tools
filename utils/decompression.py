from os.path import splitext
from os.path import getsize


def decompress(compressed, path):
    listAscii, listAsciiSize = byte_list()
    uncompressed = []
    i = 0
    filename, file_extension = splitext(path)
    f = open(filename + '.txt2', 'wb')
    w = compressed[0]
    compressed.remove(compressed[0])

    f.write(w)
    for byte_element in compressed:
        int_element = int.from_bytes(byte_element, byteorder='big')

        if int_element < listAsciiSize:
            entry = listAscii[int_element]
        elif int_element == listAsciiSize:
            entry = w + w  # ERREUR
        else:
            raise ValueError('Bad uncompressed for: %s' % byte_element)

        for byte in entry:
            if i % 2 == 1:
                f.write(byte.to_bytes(1, byteorder='big'))
            i += 1

        listAscii.insert(listAsciiSize, w + byte_element)
        listAsciiSize += 1
        w = entry
    f.close()
    return filename + '.txt2'


def file_decompression(path):
    f = open(path, "rb")
    content = []
    for i in range(int(getsize(path)/2)):
        content.insert(i, f.read(2))
    f.close()
    return decompress(content, path)
