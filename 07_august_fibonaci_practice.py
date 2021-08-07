#!/usr/bin/env python
# coding: utf-8

# In[55]:


def fibonaci():
    try:
        #f=[1,1];
        
        n = int(input("please enter the number of terms in fibonaci series : "))
        
        f = list(map(int,input("Enter the numbers : ").split(",")))
        
        print("Initial fibonacci series : ",f)
        
        if(len(f) == 2):
            
            if (n>0) and (n>2):
                
                if (f[0]==1 and f[1] ==1): 
                    
                    for i in range(2,n):
                         
                        f.append(f[i-1]+f[i-2])

                    print("fibonacci series:",f)
                
                else:
                    
                    for i in range(2,n):
                         
                        f.append(f[i-1]+f[i-2])

                    print("Not a generic one as initials are not correct")
                    print("fibonacci series:",f)

            elif n<0:

                print("can not evaluate fibonacci series for negative numbers")

            else:

                print("please give a input more than 2 else it will print intial series : ",f)
        
        elif (len(f) > 2):
            
            print("length of given list is more than 2")
            
        else:
            
            print("length of list is less than 1")
            
    except Exception as e:
        
        print("error occured : ",e)


# In[49]:


fibonaci()


# In[50]:


fibonaci()


# In[51]:


fibonaci()


# In[56]:


fibonaci()


# In[57]:


fibonaci()


# In[58]:


fibonaci()


# In[59]:


fibonaci()


# In[ ]:




