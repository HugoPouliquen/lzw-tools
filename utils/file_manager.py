def inputcontent(path):
    f = open(path, 'rb')
    content = f.read()
    f.close()
    return content


# def inputbyte(path):
#     f = open(path, "rb")
#     while True:
#         bytes = f.read(2)
#         if bytes == b'':
#             break;
#         print(bytes)
#     f.close()

def output(text, filename):
    f = open(filename, 'wb')
    for item in text:
        f.write(item)
    f.close()
    return filename
