#!/usr/bin/env python
# coding: utf-8

# # Exercise 1
# 

# In[2]:


name="Alice"
student_number="ST1002"
email="alice@gmail.com"


# In[3]:


print('Name of student:',name)
print('Student Number:',student_number)
print('Email Address:',email)


# # Exercise 2

# In[13]:


print('Name of student:',name,'\nStudent Number:',student_number,'\nEmail Address:',email)


# # Exercise 3

# In[47]:


X=14
Y=7
print('Sum of X and Y is',X+Y)
print('Difference of X and Y is',X-Y)
print('Product of X and Y is',X*Y)
print('Division of X and Y is',X/Y)


# # Exercise 4

# In[18]:


for number in range(1,6):
     print(number)
       


# # Exercise 5

# In[32]:


print('"SDK" stands for "Software Development Kit", whereas \n"IDE" stands for "Integrated Development Environment".')


# # Exercise 6

# In[34]:


print("python is an \"awesome\" language.")


# In[35]:


print("python\n\t2023") 


# In[36]:


print('I\'m from Entri.\b') 


# In[37]:


print("\65")


# In[49]:


print("\x65")


# In[39]:


print("Entri", "2023", sep="\n") 


# In[41]:


print("Entri", "2023", sep="\b") 


# In[42]:


print("Entri", "2023", sep="*", end="\b\b\b\b")


# # Exercise 7
# 

# In[50]:


num=23
textnum="57"
decimal=98.3


# In[51]:


print("Type of num:", type(num))
print("Type of textnum:", type(textnum))
print("Type of decimal:", type(decimal))



# In[54]:


sum_of_variables=num+int(textnum)+decimal
print("The sum of variables is:",sum_of_variables)


# In[56]:


print("Type of sum_of_variables:", type(sum_of_variables))


# # Exercise 8

# In[64]:


No_of_days_in_a_year=365
Hours_in_a_day=24
Minutes_in_a_hour=60


# In[65]:


total_number_of_minutes_in_a_year = No_of_days_in_a_year*Hours_in_a_day*Minutes_in_a_hour
print("Total number of minutes in a Year =",total_number_of_minutes_in_a_year)


# In[66]:


print("This code calculates the total number of minutes in a year by multiplying the number of days in a year, the number of hours in a day, and the number of minutes in an hour.")


# # Exercise 9

# In[67]:


name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")


# # Exercise 10
# py format file is also uploaded

# In[4]:


pounds=float(input("Please enter amount in pounds (£)"))
conversion_rate=1.26
dollars=pounds*conversion_rate
print(f"£{pounds} are ${dollars}")


# In[ ]:




