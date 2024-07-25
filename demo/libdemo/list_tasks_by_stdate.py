from datetime import *

f = open("tasks.txt", "rt")
ef = open("errors.txt", "wt")

tasks = []

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue
    try:
        stdate = datetime.strptime(parts[1], "%d-%m-%Y")
        if len(parts) >= 3:
            enddate = datetime.strptime(parts[2], "%d-%m-%Y")
            msg = ""
        else:
            enddate = datetime.now()
            msg = "On going"

        if stdate <= enddate:
            days = (enddate - stdate).days
            tasks.append( (stdate,enddate,parts[0],days, msg))
        else:
            raise ValueError()
    except:
        ef.write(line)


for task in sorted(tasks):
    print(f"{task[2]:50} {task[0].strftime('%d-%m-%Y')} {task[3]:3} {task[4]}")

f.close()
ef.close()

