from utility import utilities

fileName = input('Enter the file name to be opened ')
sourceString = input('Enter the string to be replaced ')
destinationString = input('Enter the replacing string ')

try:
    
    utilities.replaceString(fileName,sourceString,destinationString)
    with open(fileName) as file:
        content = file.read()
    print('Content after modification of the file is')
    print(content)

except FileNotFoundError as E:
    print('Error logged while opening file',E)
