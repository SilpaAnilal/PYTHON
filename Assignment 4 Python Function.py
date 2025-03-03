#!/usr/bin/env python
# coding: utf-8

# # Exercise 1

# In[14]:


def value(a,b=10,c=None):
    if c is None:
        print(a+b)
    else:
        print(a*b*c)


# In[18]:


#test run
value(6)
value(6,4)
value (6,4,3)


# # Exercise 2

# In[27]:


def filter_strings_by_length(lst):
    return list(filter(lambda x: len(x) >= 5, lst))


# In[28]:


#test run
string=['Alice','Bob','Charlie','Diya']
print(filter_strings_by_length(string))


# # Exercise 3

# In[30]:


expression = "3 * 5 + 2"
eval(expression)
print("The result of the given expression is:",eval(expression))
    


# # Exercise 4

# In[31]:


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primenumbers(lst):
    return list(filter(is_prime, lst))


# In[34]:


#test run
values_to_check=(2,5,6,8,29,59,128)
prime=filter_primenumbers(values_to_check)
print('Prime Numbers from the list:',prime)


# # Exercise 5

# In[39]:


words = ["world", "miracle", "magic"]
uppercase = list(map(str.upper, words))
print(uppercase) 


# In[44]:


#function
def uppercase(lst):
    return list(map(str.upper,lst))
words_ = ["cat", "elephant"]
y = uppercase(words_)
print(y)


# In[ ]:





# In[ ]:




