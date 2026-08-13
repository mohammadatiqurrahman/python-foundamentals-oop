vending = {"cola": 150, "water": 120, "coffee": 130}
item = input().lower()
if item in vending:
    print(f"{item}: {vending[item]} yen")
else:
    print("Item not available")