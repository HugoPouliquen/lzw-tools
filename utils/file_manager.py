def inputcontent(path):
    f = open(path, 'rb')
    content = f.read()
    f.close()
    return content


def output(text, filename):
    f = open(filename, 'wb')
    for item in text:
        f.write(item)
    f.close()
    return filename
