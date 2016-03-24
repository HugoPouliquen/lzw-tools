from utils.file_manager import output
from utils.file_manager import inputcontent
# from utils.file_manager import inputbyte
from os.path import splitext

# For each value return his string. chr(97) -> 'a'
def make_list():
    listAsciiSize = 255
    listAscii = []
    for i in range(listAsciiSize):
        listAscii.insert(i, i.to_bytes(2, 'big'))
    # print(listAscii)
    return listAscii, listAsciiSize


def uncompress(compressed):
    listAscii, listAsciiSize = make_list()

    # w = compressed
    # print(compressed)
    uncompressed = []
    print(int.from_bytes(compressed, byteorder='big'))
    if compressed in listAscii:
        entry = int.from_bytes(compressed, byteorder='big')
    else:
        entry = w + w[0].to_bytes(2, 'big')
    listAscii.insert(listAsciiSize, compressed)
    if entry != 0:
        uncompressed.append(chr(int.from_bytes(listAscii[entry], byteorder='big')))
    listAsciiSize += 1
    print(uncompressed)
    # entry = compressed
    # raise ValueError("Uncompressed don't work for:", compressed)
    # listAscii.insert(listAsciiSize,  w + entry[0].to_bytes(2, 'big'))
    # print( w + entry[0].to_bytes(2, 'big'))
    # print(chr(int.from_bytes(entry, byteorder='big')), end="")


def file_uncompressed(path):
    # content = inputbyte(path)
    f = open(path, "rb")
    # content = f.read(2)
    for i in range(2000):
        content = f.read(2)
        uncompress(content)
    f.close()
    # filename, file_extension = splitext(path)
    # original_file = output(uncompressed, filename + '.txt')
    # return original_file
