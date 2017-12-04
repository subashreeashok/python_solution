'''
Name : Subahree
Setno: 1
Question_no:1
Description:Finding the largest odd numbers
'''
x=raw_input("enter X: ")
y=raw_input("enter Y: ")
z=raw_input("enter Z: ")
a=int(x)
b=int(y)
c=int(z)
if(a%2!=0 and b%2!=0 and c%2!=0):#all are odd numbers  
    if(a>b and a>c):
        print("a is large")
    elif(b>a and b>c):
        print("b is large")
    else:
        print("c is large")
elif(a%2!=0 and b%2!=0 and c%2==0):#when a and b are odd numbers
            #print "c is not odd number"
    if(a>b):
        print("a is largest odd number")
    else:
        print("b is largest odd number")
elif(a%2==0 and b%2!=0 and c%2!=0):#when b and c are odd numbers
    if(b>c):
        print("b is largest odd num")
    else:
        print("c is largest odd num")
elif(a%2!=0 and b%2==0 and c%2!=0):#when a and c are odd numbers
    if(a>c):
        print("a is largest odd num")
    else:
        print("cis largest odd number")
elif(a%2==0 and b%2==0 and c%2!=0):#when c alone is an odd number
    print("c is largest odd num")
elif(a%2!=0 and b%2==0 and c%2==0):#when a alone is an odd number 
    print("a is largest odd num")
elif(a%2==0 and b%2!=0 and c%2==0):#when b alone is an odd number
    print("c is largest odd num")
else:#all are even numbers
    print("not odd number")