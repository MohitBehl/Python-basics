def func1():
    for char in "hello world":
        print(char)
def func2():
    #range(start,end,step):
    #   where start += step
    #   start < end
    for i in range(0,10,3):
        print(i)
def func3():
    lis = [10,"hello",-1,True]
    for var in lis:
        print(var)
def main():
    func3()
main()