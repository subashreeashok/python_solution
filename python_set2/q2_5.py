'''
Name : Subahree
Setno: 2
Question_no:5
Description:Sum of digits
'''
try:
  def sumDigits(s):
    sum=0
    for i in s:
      #check it is digit
      if(i.isdigit()):
        sum=sum+int(i)
    print "sum is "+str(sum)
  s=raw_input("enter Value: ")
  sumDigits(s)
except Exception as e:
  print e  