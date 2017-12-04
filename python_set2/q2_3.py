'''
Name : Subahree
Setno: 2
Question_no:3
Description:Factorial of numbers
'''

try:
  def factI(n):
    f=1
    i=1
    #finding factorial in iterative using loop 
    while(n>0):
        f=f*i
        i+=1
        n=n-1
    print "iterative value: " +str(f)  
  def factR(n):
    if((n==1) or (n==0)):
      return 1
    else:
      #finding factorial in recursive where function calls itself
      return n*factR(n-1)
  n=int(raw_input("enter a number"))
  n1=factR(n)
  print "recursive value: "+str(n1)
  factI(n)
except Exception as e:
  print e