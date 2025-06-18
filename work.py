import math


while True:   
    def A1():
        n = input("pls input your num u want to check:")
        lst = []
        for i in range(1,int(math.sqrt(n))):
            if i % n == 0:
                lst.append(i)
        
        lst.sort()
        return lst
    def perform():
        n = input("pls input your num u want to check:")
        
    def program():
        n = input("pls input your num u want to check:")

    print("=list of proplem=")
    print("1.A")
    print("2.B")
    print("3.C. ")
    s = int(input("pls input problem u want to do: "))
    

    if(s == 3):
        print(A1())
    elif(s == 2):
        print(perform())
    elif(s == 1):
        print(program())



