import os
files=os.listdir()
for f in files:
    if f.endswith('.mp4'):
        f2=f.replace('.mp4','.m4a')
        try:
            os.rename(f,f2)
        except:
            print(f+' to '+f2+' failed.')
