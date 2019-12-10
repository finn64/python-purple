import os, string, random
str_len=12+1
chars=string.digits+string.ascii_letters+"-_"

fname=__file__.replace("\\","/")
fname=fname.split("/")
fname=fname[len(fname)-1]

files=os.listdir()
for obj in files:
    if not obj==fname:
        ext=obj.split(".")
        ext=ext[len(ext)-1]
        rand=""
        for i in range(str_len-1):
            rand+=chars[random.randint(0,len(chars))]
        try:
            os.rename(obj,rand+"."+ext)
        except FileExistsError:
            rand=""
            for i in range(str_len-1):
                rand+=chars[random.randint(0,len(chars))]
            os.rename(obj,rand+"."+ext)
