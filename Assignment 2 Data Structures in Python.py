#!/usr/bin/env python
# coding: utf-8

# # List Exercise

# In[24]:


#Q1.list of 5 random numbers.
 
import random 
random_numbers=random.sample(range(1,20),5) 
print(random_numbers)


# In[44]:


#Q2.inserting 3 new values and updating the random number list
new_numbers=[2,8,6]
random_numbers.extend(new_numbers)
print("The updated random number list is:",random_numbers)


# In[47]:


#Q3.using a for loop to print each element in the list.
for i in random_numbers:
    print(i)


# # Dictionary Exercise

# In[49]:


#Q1.Creating a dictionary
person={'name':'John','age':25,'address':'New York'}
person


# In[57]:


#Q2.adding a new key value pair to dictionary
person.update({'phone': 1234567890})
person


# # Set Exercise

# In[54]:


#Q1.creating a set
x={1,2,3,4,5}
x


# In[60]:


type(x)


# In[63]:


#Q2.adding a value
x.add(6)
x


# In[64]:


#Q3.removing a value
x.remove(3)
x


# # Tuple Exercise

# In[65]:


#Q1.creating a tuple
tuple=(1,2,3,4)
tuple


# In[66]:


type(tuple)


# In[67]:


y=len(tuple)
print('The length of tuple is:',y)


# In[ ]:




