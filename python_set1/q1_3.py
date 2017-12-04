'''
Name : Subahree
Setno: 1
Question_no:3
Description:get 10 numbers and find the largest odd number 
'''

try:
  print "enter the numbers: "
  max=0
  #getting 10 numbers
  for i in range(0,10):
    num=int(raw_input())
  #print(num)
  #checking odd or not
    for j in range(0,10):
      if(num%2!=0):
        if(num>max):
          max=num
  if(max==0):
    print "numbers are not odd"
  print "largest odd number: "+str(max)
except Exception as e:
  print e 