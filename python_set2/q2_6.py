'''
Name : Subahree
Setno: 2
Question_no:6
Description:first even number
'''
try:
  def findAnEven(l):
    #to store string as list 
    list=[]
    list=l.split(',')
    print(list)
    for i in list:
      #check even or not
      if(int(i)%2==0):
        return int(i)
  l=raw_input("enter a list of integers")
  sol=findAnEven(l)
  print(sol)
except Exception as e:
  print e


