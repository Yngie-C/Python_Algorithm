#!/usr/bin/env python
# coding: utf-8

# ### No.1

# In[1]:


user_input = input("Red, Blue, Green 중에서 좋아하는 색을 입력하세요.")

if (user_input.lower() == "red"):
    user_char = "iron man"
    num = 5
elif (user_input.lower() == "blue"):
    user_char = "super man"
    num = 10
else:
    user_char = "green lantern"
    num = 3
    
i = 0
while (i < num):
    print("I'm %s" %user_char)
    i += 1


# In[2]:


while (True) :
    user_input = input("Red, Blue, Green 중에서 좋아하는 색을 입력하세요.")
    
    if (user_input.lower() == "red"):
        user_char = "iron man"
        num = 5
        break
    elif (user_input.lower() == "blue"):
        user_char = "super man"
        num = 10
        break
    elif (user_input.lower() == "green"):
        user_char = "green lantern"
        num = 3
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        continue
        
for i in range(num):
    print("I'm %s" %user_char)


# ### No.2

# In[3]:


while (1):
    print("이기창")
    break

# 편의상 break. 풀이에는 생략


# ### No.3

# In[5]:


sum = 0

while (sum <= 100):
    user_input = float(input("숫자를 입력해주세요."))
    sum += user_input
    
print(sum)


# ### No.4

# In[7]:


list_i = []
for i in range(1,50):
    if (i % 3 == 0):
        list_i.append(i)
        
print(list_i)


# In[10]:


list_i2 = []
for i in range(3, 50, 3):
    list_i2.append(i)

print(list_i2)


# ### No. 5

# In[16]:


[i for i in range(1, 50) if (i % 2 != 0)]


# ### No.6

# In[15]:


for i in range(2,20):
    for j in range(1, 20):
        break
        print(i, "X", j, "=", i*j)

# break 생략하면 됨


# ### No.7

# In[19]:


def mul_ten():
    num1 = float(input("숫자를 넣으세요"))
    return num1 * 10

mul_ten()


# ### No.8

# In[24]:


def add_num():
    num1 = float(input("숫자를 입력하세요."))
    num2 = float(input("숫자를 입력하세요."))
    
    if ((num1 + num2) > 10):
        num3 = 10
        string = "Big"
    else:
        num3 = 5
        string = "Small"
        
    [print("%s" %string) for i in range(num3)]
    
add_num()


# In[27]:


def add_num2(num1, num2):
    
    if ((num1 + num2) > 10):
        num3 = 10
        string = "Big"
    else:
        num3 = 5
        string = "Small"
        
    [print("%s" %string) for i in range(num3)]

user_input1 = float(input("숫자를 입력하세요."))
user_input2 = float(input("숫자를 입력하세요."))
add_num2(user_input1, user_input2)


# ### No.9

# In[3]:


def small_num(num1, num2):
    if (num1 <= num2):
        return num1
    else:
        return num2

user_input3 = float(input("숫자를 입력하세요."))
user_input4 = float(input("숫자를 입력하세요."))
small_num(user_input3, user_input4)


# ### No.10

# In[6]:


def sum_num3():
    num1 = float(input("숫자를 입력하세요."))
    num2 = float(input("숫자를 입력하세요."))
    num3 = float(input("숫자를 입력하세요."))
    summation = num1 + num2 + num3
    
    if (summation > 50):
        strings = "Excellent"
        repeat = 5
    elif (summation < 10):
        strings = "Bad"
        repeat = 3
    else:
        strings = "Good"
        repeat = 4
    
    [print("%s" %strings) for i in range(repeat)]
    
sum_num3()


# In[ ]:




