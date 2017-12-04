'''
Name : Subahree
Setno: 1
Question_no:9
Description:to find the value and type of  width,height and delimiter
'''

try:
  def fn(width,height,delimiter):
    w=width/2
    w1=width/2.0
    h=height/3
    a=1+2*5
    d=delimiter*5
    #finding types
    print(w,type(w))
    print(w1,type(w1))
    print(h,type(h))
    print(a,type(a))
    print(d,type(d))
    #getting input
  width=int(raw_input("enter the width:"))
  height=int(raw_input("enter the height:"))
  delimiter=raw_input("enter the delimiter:")
  #calling function fn()
  fn(width,height,delimiter)
except Exception as e:
  print e  