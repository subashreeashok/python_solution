'''
Name : Subahree
Setno: 1
Question_no:6
Description:find the sum of numbers separated by commas 
'''


try:
  num=raw_input("enter numbers: ")
  #splitting commas inbetween numbers
  num.split(',')
  sum=0
  #taking only numbers and adding
  for i in num.split(','):
     sum=sum+float(i)
  print sum
except Exception as e:
  print e
