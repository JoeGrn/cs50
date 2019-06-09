from cs50 import get_float

while True:
    print("Please enter the ammount of change required:", end = "")
    change = get_float()

    if change >= 0:
        break
    else:
        print("Provide a Positive Value")

value = round(change * 100)
quaters = value / 25
dimes = value % 25 / 10
nickles = value % 25 % 1 / 5
pennies = value % 5 / 1

total = quaters + dimes + nickles + pennies

print("{}".format(total))