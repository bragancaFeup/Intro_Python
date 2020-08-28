import io

def readArrayFromFile(filename):
    result = []
    try:
        myfile = open(filename)
    except IOError:
        raise IOError("bbb")

    for line in myfile:
        result.append(float(line))
    myfile.close()
    return result