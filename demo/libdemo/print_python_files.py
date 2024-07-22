import os


def print_file(filename):
    try:
        with open(filename) as f:
            print("-" * 50)
            print(filename)
            print("-" * 50)
            for (lineno, line) in enumerate(f.readlines(), start=1):
                print(f"{lineno:3}:{line}", end='')
    except Exception as ex:
        print("Error : ", ex)


g = os.walk(r"c:\classroom\python\demo\oop")

for (dirname, folders, files) in g:
    for f in files:
        if f.endswith(".py"):
            print_file(dirname + "\\" + f)
