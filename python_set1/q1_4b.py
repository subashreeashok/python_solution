'''
Name : Subahree
Setno: 1
Question_no:4b
Description:find the wholesale cost of books purchased 
'''


from __future__ import division
try:
  def total_cost():
    c=0
    cp=24.95
    d=40
    sp=3
    sp1=0.75
    n=int(raw_input("enter number of copies: "))
    #calculating cost for 1 copy
    if(n==1):
      c=c+cp*(d/100)*sp
    #cost for 60 copies
    else:
      c=c+(cp*(d/100)*sp1*n)
    print "the wholesale cost is " + str(c)
  total_cost()
except Exception as e:
  print e