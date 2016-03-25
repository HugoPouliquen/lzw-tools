def byte_list():
    listAsciiSize = 256
    listAscii = []
    for i in range(listAsciiSize):
        listAscii.insert(i, (i).to_bytes(2, 'big'))
    return listAscii, listAsciiSize
