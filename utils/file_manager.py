from os.path import splitext
from utils.compression import compress
from utils.pretty import pretty_compression


def file_compression(path):
    content = input(path)
    compressed = compress(content)
    filename, file_extension = splitext(path)
    lzw_file = output(pretty_compression(compressed), filename + '.lzw')
    return lzw_file


def input(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content


def output(text, filename):
    f = open(filename, 'w')
    f.write(text)
    f.close()
    return filename
