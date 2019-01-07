def func1():
    i = 0
    vars = []
    while i<10:
        vars.append(i)
        i+=1
    print("count from 0->9 ",vars)

def func2():
    i = 0
    vars = []
    while True:
        if(i>=20):
            break
        if i%2 == 0:
            vars.append(i)
        i+=1
    print("even numbers ",vars)

def func3():
    while True:
        print("in the loop")
        break
    else:
        print("outside the loop")
    while False:
        print("in the loop")
    else:
        print("outside the loop")        
def main():
    func1()
    func2()
    func3()
main()