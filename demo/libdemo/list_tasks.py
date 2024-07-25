from datetime import *

f = open("tasks.txt", "rt")
ef = open("errors.txt", "wt")

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

        days = (enddate - stdate).days
        print(f"{parts[0]:50}  {stdate.strftime('%d-%m-%Y')} {days:3} {msg}")
    except:
        ef.write(line)



f.close()
ef.close()

