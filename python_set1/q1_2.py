'''
Name : Subahree
Setno: 1
Question_no:2
Description:print string with enough leading spaces so that the last letter of the string is in column 70 of the display.
'''

try:
  def right_justify(s):
    length=len(s)
    temp=70-length
    x='_'*temp
    #str=s.rjust(70)
    print(x+s)
  s=raw_input("enter a string:")
  right_justify(s)
except Exception as e:
  print e