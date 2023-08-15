#!/usr/bin/env python
# coding: utf-8

# In[11]:


def calculator(x,y,z):
    if z == "/":
        while y != 0:
            return x/y
        else:
            print("you cannot devide by 0")
    elif z == "*":
        return x*y
    elif z == "+":
        return x+y
    else:
        return x-y

num1 = int(input("Please provide first number : "))
num2 = int(input("Please provide second number : "))
sym = input("What sign do you want to use ? - + / or * ?")

calculator(num1,num2,sym)

