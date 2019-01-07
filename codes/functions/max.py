def func(x,y,z):
    if x>y:
        if x>z:
            return x
    elif y>z:
        return y
    else:
        return z
        
def main():
    x = int(input("enter first number ?"))
    y = int(input("enter second number ?"))
    z = int(input("enter third number ?"))
    print("maximum : ",func(x,y,z))

main()