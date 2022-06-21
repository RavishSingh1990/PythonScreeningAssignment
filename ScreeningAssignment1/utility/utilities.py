

def replaceString(fileName,sourcePattern,destinationPattern):
    '''
    this function is used to a string in a file with the given string
    source string is given in sourcePattern
    new string in given in destinationPattern
    file name is given in fileName
    '''

    with open(fileName) as file:
        print('Original file content is ')
        content = file.read().replace(sourcePattern,destinationPattern)
    with open(fileName, "w") as file:
        file.write(content)
    
