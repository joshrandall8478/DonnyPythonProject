import random
def menu(n):
    good = ["Keep up the great work!","Excellent!","Great job!"]
    
    bad = ["No.Wrong answer.Keep trying.","Wrong.try again.","Wrong.Keep trying."]
    
    good = 0
    
    bad = 0
    
    dif = input("Welcome, Please enter the difficulty level(1 or 2): ")
    if dif == "1" or dif == "2":
        while(1):
            print("1 = Addition")
            print("2 = Subtraction")
            print("3 = Multiplication")
            print("4 = Division")
            print("5 = Random")
            chal = input("Enter the challenge you'd like to try: ")
            if chal == "5":
                op = str(random.randint(1,4))
            num1 = 0
            num2 = 0
            res = 0
            ans = 0
            if dif == "1":
                num1 = random.randint(0,9)
                num2 = random.randint(0,9)
            else:
                num1 = random.randint(10,99)
                num2 = random.randint(10,99)
            if num1<num2:
                sw = num1
                num1 = num2
                num2 = sw
            elif chal == "-1":
                leave(good,bad)
            elif chal == "1":
              print(f'How much is {num1}+{num2}?')
              res = num1 + num2
              
            elif chal == "2":
              print(f'How much is {num1}-{num2}?')
              res = num1 - num2
              
            elif chal == "3":
              print(f'How much is {num1}*{num2}?')
              res = num1 * num2
              
            elif chal == "4":
                if num2 == 0:
                    sw = num1
                    num1 = num2
                    num2 = sw
                print(f'How much is {num1}//{num2}?')
                res = num1 // num2
            if ans == res:
                print(good[random.randint(0,2)])
                good = good +1
            else:
                print(bad[random.randint(0,2)])
                bad = bad + 1


