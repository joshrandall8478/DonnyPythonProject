# the code reads and loads from a text file called EmailAddresses.txt
def menued():
    print('Menu')
    print('----------------------------------------')
    print('1. Look up an email address')
    print('2. Add a new name and email address')
    print('3. Change an existing email address')
    print('4. Delete a name and email address')
    print('5. Quit the program')

def lookup(y,dicti):
    if y in dicti:
        response = dicti[y]
    else:
        response = 'The specified name was not found'
def adding(y,z,dicti):
    t = 'that name already exists'
    if y in dicti:
        return t
    else:
        dicti[y] = z
        return dicti
def changing(y,z,dicti):
    t = 'not here'
    if y in dicti:
        del dicti[y]
        dicti[y] = z

        return dicti
    else:
        return t
def deleting(y,dicti):
    t = 'not here'
    if y in dicti:
        del dicti[y]


        return dicti
    else:
        return t
def save(lsst):
    with open('EmailAddresses.txt', 'w') as output:
        for i in range(len(lsst)):
            prob = list(lsst[i])

            for ii in range(len(prob)):
                output.write(prob[0]+' '+prob[1]+'\n')
    return output
def load():
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
    dicti = load()
    for i in range(3000):
        menued()
        x = int(input('Enter your choice: ', ))

        if x == 1:
            y = input('Enter name: ', )
            search = lookup(y,dicti)
            print(search)

        if x == 2:
            y = input('Enter name: ', )
            z = input('Enter email address: ', )
            add = adding(y,z,dicti)


        if x == 3:
            y = input('Enter name: ', )
            z = input('Enter email address: ', )
            change = changing(y, z,dicti)
            print('information updated')

        if x == 4:
            lists = []
            y = input('Enter name: ', )
            delete = deleting(y,dicti)
            #lst = list(delete.items())

        if x ==5:
            lsst = list(dicti.items())
            wrt = save(lsst)
            break
main()
