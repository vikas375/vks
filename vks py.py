#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a 
# comma-separated sequence on a single line.


# In[25]:


nl=[]
for x in range(2000,3200):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))


# In[26]:


## Write a Python program to reverse a word after accepting the input from the user.


# In[27]:


word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# In[28]:


def reverse(string): 
    string = string[::-1] 
    return string 
  
s = "Vikas Pratap Singh"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using extended slice syntax) is : ",end="") 
print (reverse(s)) 


# In[29]:


## Create the below pattern using nested for loop in Python.
n=9;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[43]:



print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")


# In[ ]:





# In[ ]:




