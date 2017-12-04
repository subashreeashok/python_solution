''' 
 Name : Subahree 
 Setno: 2
 Question_no:8
 Description: using eval 
 ''' 



import math
try:
    def eval_loop(evalue):
        x=eval(evalue)
        print(x)
    evalue=raw_input("enter eval: ")
    while evalue=="done":
        print("exited")
        break
    eval_loop(evalue)    
    #evalue=raw_input("enter eval: ")
except Exception as e:
   print(e)    
