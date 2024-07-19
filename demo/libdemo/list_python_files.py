
import os

g = os.walk(r"c:\classroom\python\demo")

for (dirname, folders, files) in g:
    for f in files:
        if f.endswith(".py"):
            print( dirname + "\\" + f)


