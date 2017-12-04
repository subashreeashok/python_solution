'''
Name : Subahree
Setno: 2
Question_no:2 
'''
from __future__ import division
try:
  def is_power(a,b):
    d=a/b
    if(a%b==0 and d%b==0):
      print "true"
    else:
      print "false"
      
  a=int(raw_input("enter A: "))
  b=int(raw_input("enter B: "))
  is_power(a,b)
except Exception as e:
  print e