
st = "Srikanth Pragada"

valid = True
for c in st:
    if not(c.isalpha() or c == " "):
        print("Invalid Name")
        valid = False
        break

if valid:
    print("Valid Name")


