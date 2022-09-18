import os
files=os.listdir()
for item in files:
    try:
        for file in os.listdir(dir):
            files.append(os.path.join(dir,file))
    except:
        next
out=open(os.path.basename(os.path.abspath(""))+".txt","w")
out.write("\n".join(files))
out.flush()
out.close()
