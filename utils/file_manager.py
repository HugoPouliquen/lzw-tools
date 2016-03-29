def inputContent(path):
    """
    Purpose: Extract byte content from file
    Description: Open file in read and byte mode and then save his content
    Param: path of file
    Return: content of file
    """
    f = open(path, 'rb')
    content = f.read()
    f.close()
    return content


def output(compressed, filename):
    """
    Purpose: Write byte content in file
    Description: Open file in write and byte mode and then write each item
    of compressed text in file
    Param: compressed text and name of the file to write
    Return: filename
    """
    f = open(filename, 'wb')
    for item in compressed:
        f.write(item)
    f.close()
    return filename
