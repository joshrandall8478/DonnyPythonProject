def menu():
    print("Menu")
    print("-------------------------")
    print("1. Look up an email")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit")
    opt = int(input("Enter the command you'd like to use: "))
    return opt


def lookup(file):
    name = str(input("Enter a name: "))
    if name in file:
        print("Name: {}".format(name))
        print("Email: {}".format(file))
        print("")
    else:
        print("Name has not been found")


def add(file):
    name = str(input("Enter a name: "))
    email = str(input("Enter an email address: "))
    file.append(name)
    print("Name and email have been added")
    print("")


def change(file):
    name = str(input("Enter name: "))
    if name not in email:
        print("name not found")
        return None
    email = str(input("Enter new email address"))
    file.append(name)
    print("")


def delete(email):
    name = str(input("Enter name: "))
    if name not in email:
        print("name not found")
        print("")
        return None
    del email[name]
    print("information deleted")
    print("")


def save(email):
    file = open("EmailAddresses.txt", "r")
    names = list(email.keys())
    for i in range(len(names)):
        file.write(names[i] + " " + email[names[i]])
        if len(names) - i > 1:
            file.write("\n")


def read(email):
    file = email.read()
    for i in range(len(file)):
        ent = file[i].split(" ")
    return email


def main():
    file = open("EmailAddresses.txt", "a")
    run = True
    while run:
        menu()
        if menu() == 1:
            lookup(file)
        if menu() == 2:
            add(file)
        if menu() == 3:
            change(file)
        if menu() == 4:
            delete(file)
        if menu() == 5:
            save(file)
            print("Information Saved")
            run = False


main()
