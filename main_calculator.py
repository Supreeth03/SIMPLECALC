#!/usr/bin/env python
# coding: utf-8

# In[6]:


import operators as op
while(True):
    num1=int(input('enter 1st no: '))
    num2=int(input('enter 2nd no: '))
    ops=input('Enter operation you want to perform: +,-,/,* : ')
    if(ops=='+'):
        op.add(num1,num2)
    elif(ops=='-'):
        op.sub(num1,num2)
    elif(ops=='*'):
        op.mul(num1,num2)  
    elif(ops=='/'):
        op.div(num1,num2)
    else:
        print('invalid operator')
    calc=input('want to perform an operation again:(yes/no)')
    if(calc.lower()=='no'):
        break 
    else:
        pass


# In[ ]:





# In[ ]:





# In[ ]:




