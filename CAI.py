mode = 0


def menu(n):
    if 1 <= n <= 4:
        return int(n)


print("Enter option")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

choice = menu(int(input("Choice: ")))
while choice is None:
    choice = menu(int(input("Please enter an actual value: ")))

print("You chose " + str(choice))
