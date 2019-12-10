import os, random, string, time
charset = list(":;⁃♠|_‒‾⎸⎹╮╰╯└⟍⟋┌┐⚫▄♥▏╭╳🞅⚘▕ "+string.digits+"◆╋▒|π◥ ▌▄‾_⎸▗┗┓▂┏┻┳┫▎▌▐⎯▀▄┛▖▝┛🙿@" + string.ascii_letters + "#$%&’()*+,-./"+" "*10)
art="""
/--\\     |---\\ ----  |        /---\\        \\   /
\\ /  --- |___/  |   -|--      |     |    |  \\ / 
 / \\     |   \\  |    |        |  __ |    |   |
\\__/     |___/ ----  \\__      \\___/  \\__/    |"""
line=1
cols = os.get_terminal_size().columns
lines = os.get_terminal_size().lines

col=1
line=1
for i in range(0,len(charset)-1):
    for c in art:
        if c=="\n":
            if line<lines:
                print("")
                line+=1
                col=1
        elif col==cols:
            if line<lines:
                print("")
                col=1
            else:
                break
        else:
            if c in charset:
                col+=1
                if charset.index(c)>i:
                    max=3
                    if len(charset)-i-1<=2:
                        max=len(charset)-i-1
                    print(end=charset[i+random.randint(0,max)])
                else:
                    print(end=c)
    print(end="\n"*(lines-line))
    time.sleep(0.01)
i = len(charset)-1
for c in art:
    if c=="\n":
        try:
            if (line+1)<lines:
                print(end="\n")
                line+=1
                col=1
        except:
            continue
    elif col==cols:
        if line<lines:
            print("")
            col=0
        else:
            continue
    else:
        if c in charset:
            col+=1
            if charset.index(c)>i:
                print(end=charset[+random.randint(-1,)])
            else:
                print(end=c)
print(end="\n"*(lines-line))
time.sleep(0.0685)
print()