def areaRectangle(length,breadth):
    return length*breadth
def test():
    pass
def main():
    length = int(input("enter length of rectangle ?"))
    breadth = int(input("enter breadth of rectangle ?"))
    area = areaRectangle(length,breadth)
    print("length : ",length ,"\nbreadth : ",breadth,"\narea : ",area)
    test()

main()