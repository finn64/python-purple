import os
files = os.listdir()
from_ext = input("from extension: ")
to_ext = input("to extension: ")
from_ext = from_ext.strip(" \t.*\\/:?<>|")
to_ext = to_ext.strip(" \t.*\\/:?<>|")
for f in files:
    if f.endswith("."+from_ext):
        f2 = f.split(".")
        f2.remove(f2[len(f2)-1])
        f2 = ".".join(f2) +"."+ to_ext
        try:
            os.rename(f,f2)
        except:
            print(f+ " to " +f2+ " failed.")
