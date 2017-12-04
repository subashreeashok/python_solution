'''
Name : Subahree
Setno: 2
Question_no:7
Description:palindrome or not
'''

try:
 def isPalindrome(s):
   length=len(s)
   i=0
   a='true'
   while(length>0):
     if s[i]==s[length-1]:
       i=i+1
       length=length-1
       return a
     else:
       print "false"
       break
 s=raw_input("enter a string:")
 x=isPalindrome(s)
 print(x)
except Exception as e:
    print e