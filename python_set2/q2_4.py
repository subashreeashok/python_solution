'''
Name : Subahree
Setno: 2
Question_no:4
Description:convert binary  to decimal
'''
try:
  def dec_fn(b):
    d=0
    for i in b:
      #converting to decimal value
      d = d*2 + int(i)
    print d
  b=raw_input("enter value: ")
  dec_fn(b)
except Exception as e:
  print e