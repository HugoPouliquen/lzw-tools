from os.path import basename
from os.path import splitext
from utils.compression import compress
from utils.pretty import pretty_compression


def file_treat(path):
    content = input(path)
    compressed = compress(content)
    filename = output(compressed, filename_extract(path) + '.lzw')
    return filename


def filename_extract(filename):
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
    f.write(pretty_compression(text))
    f.close()
    return filename
