'''
Name : Subahree
Setno: 1
Question_no:8
Description:ratio of two list 
'''

try:
 def getRatios(vect1,vect2):
     len_v1=len(vect1)
     len_v2=len(vect2)
     #to store the result as list
     vect3=[]
     i=0
     if(len_v1==len_v2):
       #to find ratio of list
       while(i<len_v1):
         r=int(vect1[i])/int(vect2[i])
         vect3.insert(i,float(r))
         i+=1
       print vect3
 l1=raw_input("enter list 1")
 l2=raw_input("enter list 2")
 #to store string as list
 vect1=[]
 vect1=l1.split(',')
 vect2=[]
 vect2=l2.split(',')
 getRatios(vect1,vect2)
except Exception as e:
    print(e)