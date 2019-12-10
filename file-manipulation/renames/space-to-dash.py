import os
files=os.listdir()
for f in files:
    if f.find(" ")>-1 or f.find("_")>-1:
        f2=f.replace(" ","-").replace("_","-")
        try:
            os.rename(f,f2)
        except:
            print(f+" to "+f2+" failed.")
