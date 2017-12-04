'''
Name : Subahree
Setno: 1
Question_no:7
Description:to find the equal strings
'''


try:
  def isIn(str,str1):
    #comparing equal strings
    if(str==str1 or str1==str):
      print "true"
    else:
      print "false"
  str=raw_input("enter string:")
  str1=raw_input("enter second string:")
  isIn(str,str1)
except Exception as e:
  print e
