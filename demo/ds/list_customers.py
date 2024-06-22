data = [ "Jack,383883333", "Scott,38382222",
         "Andy,919933323", "Ben-392922222",
         "Andy,989898989"
         ]

customers = {}
for cust in data:
    if ',' not in cust:
        continue

    name, mobile = cust.split(",")
    customers[name] = mobile

for name, mobile in sorted(customers.items()):
    print(f"{name:15} {mobile}")

