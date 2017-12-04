''' 
 Name : Subahree 
 Setno: 2
 Question_no:9a
 Description:sqrt using newton formula
 ''' 
try:
    #calculating using newton sqrt
    def NewtonSqrt(): 
        y = (x + a/x)/2
        print(y)
    x=float(raw_input("enter x:"))
    a=float(raw_input("enter a:"))
    NewtonSqrt()
except Exception as e:
   print(e)
