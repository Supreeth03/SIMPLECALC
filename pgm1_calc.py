#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(a,b):
    print(a+b)


# In[2]:


def sub(a,b):
    print(a-b)


# In[3]:


def mul(a,b):
    print(a*b)


# In[4]:


def div(a,b):
    print(a/b)


# In[10]:


while(True):
    num1=int(input('enter 1st no: '))
    num2=int(input('enter 2nd no: '))
    ops=input('Enter operation you want to perform: +,-,/,* : ')
    if(ops=='+'):
        add(num1,num2)
    elif(ops=='-'):
        sub(num1,num2)
    elif(ops=='*'):
        mul(num1,num2)  
    elif(ops=='/'):
        div(num1,num2)
    else:
        print('invalid operator')
    calc=input('want to perform an operation again:(yes/no)')
    if(calc.lower()=='no'):
        break
    else:
        pass


# In[ ]:




