import base64, os

S = os.sep

print('--Convert base64 strings to files')
def get(pront):
    answer = ''
    while answer == '':
        print(pront)
        answer = input()
        answer = answer.strip('"')
        print('')
    return answer
notFound = True
while notFound:
    filename = get('Enter list file name/path.')
    ext = get('Enter extension type.')

    try:
        inFile = [open(filename,'r').read()]
        notFound = False
    except FileNotFoundError:
        print(end='File not found, please ')
        filename = get('Enter dir name/path.')
i=0
for file in inFile:
    b64string = base64.b64decode(file)
    thisfilename = filename + ext
    try:
        outFile = open(thisfilename,'w')
        outFile.write(b64string)
            
    except:
        print('Couldn\'t write',os.path.dirname(filename) +S+ str(i))
    try:
        outFile.close()
    except:
        continue
    i+=1
inFile=''
input('"{0}" written to "{1}"\nenter to exit...\n'.format(dirname,outdir))
