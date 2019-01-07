temp = "hello"
#type() is used to find class of a particular object
print("temp : ",temp," type : ",type(temp))

temp = "123"
print("temp : ",temp," type : ",type(temp))

temp = int(temp)
print("temp : ",temp," type : ",type(temp))

exp = "12-25+63"
print('let the expression be "12-25+63"')
val = eval(exp);
print('answer using eval function = '+str(val)) #example of eval function

arr = [12,1,-60,10,63,123] #list data-struture
print("contents : " ,arr , " max : ",max(arr)," min : ",min(arr))

arr = ["a","abc","zfg","hklas"]
print("contents : " ,arr , " max : ",max(arr)," min : ",min(arr))

import math #functions using math function
print("math.pow(3,4):",math.pow(3,4))
print("math.sqrt(65):",math.sqrt(65))