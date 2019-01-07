def sum(*var):
    result = 0;
    #for temp in var:
    #   result += temp;
    i = 0;
    while(i<len(var)):
        result += var[i];
        i+=1
    return result
def main():
    print(sum(1,2,3,4,5,6,7,8,9,10))
main()