import os
files=os.listdir()
for item in files:
    try:
        for itm in os.listdir(item):
            files.append(item+"\\"+itm)
    except:
        next
out=open(os.path.basename(os.path.abspath(""))+".txt","w")
out.write("\n".join(files))
out.flush()
out.close()
