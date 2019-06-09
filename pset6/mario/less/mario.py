from cs50 import get_int

while True:
    print("Specify Pyramid Height: ", end = "")

    pyramidheight = get_int()

    if pyramidheight > 0 and pyramidheight <=23:
            break

    else:
            print("Provide a Number between 0 and 23")

for i in range (pyramidheight):
    for j in range (pyramidheight - i - 1):
        print(" ", end = "")
    for k in range (i + 1):
        print("#", end = "")
    print("")


