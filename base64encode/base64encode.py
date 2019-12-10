import base64
EXT='.b64.txt'
EXIT_STRING = 'h?q'
BAD_CHARS = ':*?"<>|\t\n'
print('--Convert to base64 string')
def getfn():
    answer = ''
    while answer == '':
        answer = input('enter file name/path, or "'+EXIT_STRING+'" to exit...\n')
        answer = answer.strip(BAD_CHARS)
        print('')
    return answer
notFound = True
while notFound:
    filename = getfn()
    if filename == EXIT_STRING:
        notFound = False
        exit()
    else:
        try:
            inFile = open(filename,'rb').read()
            notFound = False
        except FileNotFoundError:
            print(end='File not found, please ')
            getfn()

b64string = base64.b64encode(inFile).decode("utf-8")
outFile = open(filename+EXT,'w')
outFile.write(b64string)
outFile.close()
inFile=''
input('"{0}" written to "{0}{1}"\nenter to exit...\n'.format(filename,EXT))
