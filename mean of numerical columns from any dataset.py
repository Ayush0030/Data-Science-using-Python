#!/usr/bin/env python
# coding: utf-8

# In[53]:



import numpy as np
import pandas as pd

df=pd.read_excel("Rough.xlsx")
df

array=np.array(df)
array

# iterator Function below
def iterator():
    new_array=[]
    global column_names
    flag=0
    flag2=0
    column_names=[]
    global repeater
    repeater=0
    for i in range(array.shape[0]):
        repeater=0
        for j in range(array.shape[1]):
            if(isinstance(array[i,j], int) or isinstance(array[i,j],float)):
                repeater=repeater+1
                new_array.append(array[i][j])
                if(flag==0):
                    column_names.append(df.columns[j])
        flag=1
    new_array=np.array(new_array)
    return new_array

new_array=iterator()

new_array.shape

# Mean Function Below
def mean():
    sum=0
    mean=0
    x=np.arange(0,new_array.shape[0],repeater)
    global array_means
    array_means=[]
    for j in range(repeater):
        for i in x+j:
            sum=sum+new_array[i]
        mean=sum/len(x)
        array_means.append(mean)
    array_means=np.array(array_means)
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    array_means=array_means.astype(float)
    array_means
    return array_means
column_names=np.array(column_names)
print(column_names)
array_means=mean()
array_means
pd.DataFrame(array_means.reshape(-1,repeater),columns=[column_names],index=["mean"])

