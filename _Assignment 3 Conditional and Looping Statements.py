#!/usr/bin/env python
# coding: utf-8

# # Exercise 1
# Month Names

# In[1]:


month=int(input("Enter the month: "))

if month==1:
    print("Month 1 is January")
elif month==2:
    print("Month 2 is February")
elif month==3:
    print("Month 3 is March")
elif month==4:
    print("Month 4 is April")
elif month == 5:
    print("Month 5 is May")
elif month==6:
    print("Month 6 is June")
elif month==7:
    print("Month 7 is July")
elif month==8:
    print("Month 8 is August")
elif month==9:
    print("Month 9 is September")
elif month==10:
    print("Month 10 is October")
elif month==11:
    print("Month 11 is November")
elif month==12:
    print("Month 12 is December")
else:
    print("Invalid.")


# # Exercise 2

# In[2]:


age = int(input("Enter your age: "))

if age < 16:
    ticket_price = 6 / 2
elif age >= 60:
    ticket_price = 6 / 3
else:
    ticket_price = 6

print(f"Your ticket costs £{ticket_price: }")


# # Exercise 3
# BodyMassIndex

# In[3]:


Weight=float(input("Enter your weight(kg): "))
Height=float(input("Enter your height(m): "))

BMI= Weight/(Height**2)
print(f" Your BMI is:{BMI}")
if BMI<18.5:
    print('You are in the "underweight" range.')
elif 18.5<= BMI <= 24.9:
    print('You are in the "Normal" range.')
elif 25 <= BMI <= 29.9:
    print('You are in the "overweight" range.')
else:
    print('You are in the "obese" range.')


# # Exercise 4

# In[4]:


number1=input("Enter first number:")
number2=input("Enter second number:")
number3=input("Enter third number:")

greatest_number=max(number1,number2,number3)
print(f"The greatest number is:{greatest_number}")


# # Exercise 5

# In[5]:


Number= int(input("Enter a number: "))
factorial=1
if Number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for n in range (1,Number+1):
        factorial*=n
    print(f"The factorial of {Number} is {factorial}.")


# # Exercise 6

# In[6]:


num = int(input("Enter a number to reverse: "))
Reversed_number=0
while num:
    Reversed_number=Reversed_number*10+num%10
    num//=10
print(f"The reversed number is {Reversed_number}.")


# # Exercise 7

# In[7]:


numb = int(input("Enter a number to find its multiples: "))
count = int(input("No:of times to multiply: "))

print(f"The first {count} multiples of {numb} are:")
for i in range(1, count + 1):
    print(numb * i)


# # Exercise 8

# In[8]:


while True:
    user_input = input("Enter your input: ")  
    if user_input == 'done': 
        print("Done")
        break  
    else:
        print(user_input)


# # Exercise 9

# In[9]:


for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  
    elif i % 3 == 0:
        print("Fizz")  
    elif i % 5 == 0:
        print("Buzz")  
    else:
        print(i)  


# # Exercise 10
# 

# In[10]:


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


# In[ ]:




