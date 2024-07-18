f = open('customers.txt', "rt")

sname = input("Enter customer name :").upper()

while True:
    line = f.readline()
    if line == "":  # EOF
        print("Sorry! Not found!")
        break

    line = line.strip()   # remove \n at the end

    # check whether it has , and ignore the line, if not found
    if line.find(",") == -1:
        continue

    name, phone = line.split(',')
    if name.upper() == sname:
        print('Phone number :', phone)
        break

f.close()
