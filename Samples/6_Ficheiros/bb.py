def readArrayFromFile(filename):
    result = []
    myfile = open(filename)
    for line in myfile:
        result.append(float(line))
    myfile.close()
    return result