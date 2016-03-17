from os.path import basename
from os.path import splitext
from utils.compression import compress


def file_treat(filename):
    content = input(filename)
    compressed = compress(content)
    filename = output(compressed, filename_extracted(filename) + '.lzw')
    return filename


def filename_extracted(filename):
    base = basename(filename)
    name = splitext(base)[0]
    return name


def input(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content


def output(text, filename):
    f = open(filename, 'w')
    for item in text:
        f.write(str(item))
        f.write(' ')
    f.close()
    return filename
