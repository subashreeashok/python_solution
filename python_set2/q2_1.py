'''
Name : Subahree
Setno: 2
Question_no:1
Description:GCD of numbers 
'''


try:
  def gcd_fn(num1,num2):
    if(num2==0):
      print "GCD is "+str(num1)
    elif((num1%num2)==0):
      print "GCD is "+str(num2)
    else:
      x=num1%num2#Reminder stored inside x
      gcd_fn(num2,x)#num2 and reminder is passed as input to gcd_fn
  num1=int(raw_input("number 1:"))
  num2=int(raw_input("number 2:"))
  gcd_fn(num1,num2)
except Exception as e:
  print e