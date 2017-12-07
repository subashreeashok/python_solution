'''
Name: subashree
setno:1
Qno:8
Description:find the ratio of two vectors
'''

def getRatios(vect1,vect2):
    try:
     print(vect1)
     print(vect2)
     length=len(vect1)
     length1=len(vect2)
     vect3=[]
     i=0
     if(length==length1):
       while(i<length):
         a=float(vect1[i])/float(vect2[i])
         vect3.insert(i,a)
         i+=1
       print(vect3)
     else:
       print("length not equal")
    except Exception as e:
        print(e)
a=raw_input("enter list")
b=raw_input("enter list")
vect1=a.split(',')
vect2=b.split(',')
getRatios(vect1,vect2)