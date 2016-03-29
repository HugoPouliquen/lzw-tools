from os.path import splitext
from utils.file_manager import output
from utils.file_manager import inputContent
from utils.make_list import byteList


def compress(bytes_text):
    """
    Purpose: Compress a byte text file
    Description:
    Each value of the text file is converted and concatenated into two bytes.
    If concatenated bytes are present in the ASCII list, the program continues.
    Else, the concatenated bytes are added to the ASCII list. Also, w is added
    to the compressed array and assign to c
    Param: Text (in byte) to compress
    Return: The compressed content
    """
    w = bytes()
    list_ascii, list_ascii_size = byteList()
    compressed = []
    for c in bytes_text:
        c = c.to_bytes(2, 'big')
        wc = w + c
        if wc in list_ascii:
            w = wc
        else:
            list_ascii.insert(list_ascii_size, wc)
            compressed.append(list_ascii.index(w).to_bytes(2, 'big'))
            list_ascii_size += 1
            w = c
    return compressed


def fileCompression(path):
    """
    Purpose: Create a compressed file
    Description: Extract and compress the content of the file in param to
    create a new .lzw file
    Param: Path of file to compress
    Return: LZW file name
    """
    content = inputContent(path)
    filename, file_extension = splitext(path)
    compressed = compress(content)
    lzw_file = output(compressed, filename + '.lzw')
    return lzw_file
