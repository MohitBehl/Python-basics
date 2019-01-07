message = "hello"
def indices():
    print("indices of ",message," are")
    l = len(message)
    i = 0
    while(i<len(message)):
        print(str(i)," ",message[i]," ",0-l)
        l-=1
        i+=1

def operations():
    print("concatenation : ","hello"+"world")
    print("multiplication :"," hello"*5)

def basic_funcs():
    print("message : ",message)
    print("length : ",len(message))
    print("capitalized message : ",message.capitalize())
    print("count of l : ",message.count('l'))

def fun_in():   #membership operator
    print("message : ",message)
    print("ell in message : ",str("ell" in message))
    print("a in  message : ",str("a" in message))

def slicing():
    #string_message[start:end:inc]
    print("message : ",message)
    print("sub_str 0-1 : ",message[0:2])
def main():
    slicing()
main()