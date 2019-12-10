import os
ext='.txt'
items = (item for item in os.listdir())
try:
    filename = os.path.basename(os.path.abspath('.'))
except:
    filename = 'out'

output = ''
for item in items:
    if os.path.isdir(item):
            item += os.sep  #dir end with /
    output += '.' + os.sep+item+'\n'  #add this item
    if os.path.isdir(item):
        try:
            items2 = (item2 for item2 in os.listdir(item))  #get items in dir
            for item2 in items2:
                output += '\n    d .' + os.sep+item+os.sep+item2 + os.listdir(item + os.sep + item2)    #add to string
        except:
            pass
    
output += '\n'
n=''
fail=1
outf=None
while fail:
    try:
        outf = open(filename+n+ext,'w') #open file
    except:
        if n=='':
            n=0
        else:
            n+=1
    finally:
        fail=0
outf.write(output)  #write output
outf.flush()
outf.close()    #flush and close
