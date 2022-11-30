#For this program to work, please make a text file and name it EmailAddresses.txt

def menu():
    print("Menu")
    print("-------------------------")
    print("1. Look up an email")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit")
    return ""

def lookUpEmail(y,dicti):
    if y in dicti:
        response = dicti[y]
        print(response)
        return ""
    else:
        print("The specified name was not found")
        return ""

def addEmail(y,z,dicti):
    if y in dicti:
        print("That name already exists")
        return ""
    else:
        dicti[y] = z
        return ""
    
def changeEmail(y,z,dicti):
    if y in dicti:
        del dicti[y]
        dicti[y] = z
        print("Email changed")

        return ""
    else:
        print("Name does not exist")
        return ""
    

def deleteEmail(y,dicti):
    if y in dicti:
        print("Name and Email deleted")
        del dicti[y]
        return ""
    else:
        print("Name does not exist")
        return ""

    

def saveEmail(lsst):
    with open('EmailAddresses.txt', 'w') as output:
        for i in range(len(lsst)):
            prob = list(lsst[i])

            for ii in range(len(prob)):
                output.write(prob[0]+' '+prob[1]+'\n')
    return ""
    

def read():
    dicti = {}
    lid = []
    count = 0
    with open("EmailAddresses.txt", "r") as file:
        texx = file.read()
        for line in file:
            line.split()
            lid.append(line)
    newlist = []
    for i in lid:
        no = i.replace('\n','')
        newlist.append(no)
    tlist = []

    for i in range(0,len(newlist)):
        tlist = newlist[i]
        Tist = tlist.split()
        dicti[Tist[0]] = Tist[1]
    return dicti

def main():
    dicti = read()
    run = True
    while run:
        menu()
        print("\n")
        opt = int(input("Enter the command you'd like to use: "))
        if opt == 1:
            y = input('Enter name: ', )
            search = lookUpEmail(y,dicti)
            print(search)
            
        if opt == 2:
            y = input('Enter name: ', )
            z = input('Enter email address: ', )
            add = addEmail(y,z,dicti)
            
        if opt == 3:
            y = input('Enter name: ', )
            z = input('Enter email address: ', )
            change = changeEmail(y, z,dicti)
            print('information updated')
            
        if opt == 4:
            lists = []
            y = input('Enter name: ', )
            delete = deleteEmail(y,dicti)
            
        if opt == 5:
            lsst = list(dicti.items())
            wrt = saveEmail(lsst)
            print("Information Saved")
            break
main()



