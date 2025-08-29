#%%

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


'''
Submit your solutions in pdf format, with code and plots supporting your answers.
machine_data contains raw data of a part from 3 manufactures A, B, C
The system is run to failure under load
The load and the operation time is provided in each row

What is the range of load and time during operation for each manufacturer?
What is the most expected load value?
How are the load and time related?
Which distribution best describes the load?
Which distribution best describes the time?

Which manufacturer has the best performance and why?

'''
#%%
# read the data file into a dataframe
df = pd.read_csv('machine_data-1.csv')
print(df)

print(df.shape)

#%% 
'''
Drop the index
'''
df = pd.read_csv('machine_data-1.csv', usecols=[1,2,3])
#use only cols 1, 2, 3 not 0
#%%
'''
Extract data for a given manufacturer
'''
#changed manufacturef to manufacturer in csv
df['manufacturer'] = df['manufacturer']
grpByManu = df.groupby('manufacturer')

dfa = grpByManu.get_group('A')
dfb = grpByManu.get_group('B')
dfc = grpByManu.get_group('C')


#%%
#changed manufacturef to manufacturer in csv
df['manufacturef'] = df['manufacturer']
#couldnt do dfc, becuase csv was using a lower 'c', so i changed all char under manufacturer to uppercase chars with ->
df['manufacturer'] = df['manufacturer'].str.upper()
#reload data to dataframe ->
grpByManu = df.groupby('manufacturer')

dfa = grpByManu.get_group('A')
dfb = grpByManu.get_group('B')
dfc = grpByManu.get_group('C')


#%%

loada = dfa['load']
timea = dfa['time']

loadb = dfb['load']
timeb = dfb['time']

loadc = dfc['load']
timec = dfc['time']

#%% #A
'''
Is there a relationship between load and time
'''
plt.scatter(loada, timea)
plt.title("Relation between load and time")
plt.xlabel("Load for A")
plt.ylabel("Time for A")
plt.show()
'''
the more load, the shorter time.
'''

#%% #B
plt.scatter(loadb, timeb)
plt.title("Relation between load and time")
plt.xlabel("Load for B")
plt.ylabel("Time for B")
plt.show()
'''
the more load, the shorter time.
'''

#%% #C
plt.scatter(loadc, timec)
plt.title("Relation between load and time")
plt.xlabel("Load for C")
plt.ylabel("Time for C")
plt.show()
'''
the more load, the shorter time.
'''

#%%
'''
Characteristics of data
mean, median, mode
'''
dfa['load'].mean()
dfa['load'].median()
dfa['load'].mode()

dfa['time'].mean()
dfa['time'].median()
dfa['time'].mode()


#%%
dfb['load'].mean()
dfb['load'].median()
dfb['load'].mode()

dfb['time'].mean()
dfb['time'].median()
dfb['time'].mode()

#%%
dfc['load'].mean()
dfc['load'].median()
dfc['load'].mode()

dfc['time'].mean()
dfc['time'].median()
dfc['time'].mode()

#%%
temp = dfa['load'].max()-dfa['load'].min()
print("Load range for A: ", dfa['load'].max(),"-",dfa['load'].min(), "= ", temp)
temp = dfa['time'].max()-dfa['time'].min()
print("Time range for A: ", dfa['time'].max(),"- ",dfa['time'].min(), "= ", temp)
print(' ')

temp = dfb['load'].max()-dfb['load'].min()
print("Load range for B: ", dfb['load'].max(),"-",dfb['load'].min(), "= ", temp)
temp = dfb['time'].max()-dfb['time'].min()
print("Time range for B: ", dfb['time'].max(),"- ",dfb['time'].min(), "= ", temp)

print(' ')

temp = dfc['load'].max()-dfc['load'].min()
print("Load range for C: ", dfc['load'].max(),"-",dfc['load'].min(), "= ", temp)
temp = dfc['time'].max()-dfc['time'].min()
print("Time range for C: ", dfc['time'].max(),"- ",dfc['time'].min(), "= ", temp)

#%% #ALoad
'''
How is load distributed
Why does it matter
uniform, normal, exponential, weibull
'''
dfa[['load']].plot(title='A', kind='hist', bins=10 , edgecolor='black')

'''
Seems to have an normaldisturbed load, with a symmetrical middlepoint
'''

mean  = dfa['load'].mean()
median = dfa['load'].median()
skew  = dfa['load'].skew()      # 0 ≈ symmetrisk, >0 högerskev, <0 vänsterskev
print(f"HistA, mean={mean:.2f}, median={median:.2f}, skew={skew:.3f}")
'''
if skew = 0, its symmertrical.
if skew > 0, its a right-skew
if skew < 0, its a left-skew
'''

#%% #ATime
'''
How is time distributed
Why does it matter
uniform, normal, exponential, weibull
'''
dfa[['time']].plot(title='A', kind='hist', bins=10 , edgecolor='black')

'''
Seems to have an normaldisturbed time, with a symmetrical middlepoint
'''

mean  = dfa['time'].mean()
median = dfa['time'].median()
skew  = dfa['time'].skew()      # 0 ≈ symmetrisk, >0 högerskev, <0 vänsterskev
print(f"HistA, mean={mean:.2f}, median={median:.2f}, skew={skew:.3f}")
'''
if skew = 0, its symmertrical.
if skew > 0, its a right-skew
if skew < 0, its a left-skew
'''


#%% #B
'''
How is load distributed
Why does it matter
uniform, normal, exponential, weibull
'''
dfb[['load']].plot(title='B', kind='hist', bins=10, edgecolor='black')

'''
Seems to have an normaldisturbed load, with a symmetrical middlepoint
'''

mean  = dfb['load'].mean()
median = dfb['load'].median()
skew  = dfb['load'].skew()      # 0 ≈ symmetrisk, >0 högerskev, <0 vänsterskev
print(f"HistB, mean={mean:.2f}, median={median:.2f}, skew={skew:.3f}")
'''
if skew = 0, its symmertrical.
if skew > 0, its a right-skew
if skew < 0, its a left-skew
'''
#%% #BTime
'''
How is time distributed
Why does it matter
uniform, normal, exponential, weibull
'''
dfb[['time']].plot(title='B', kind='hist', bins=10 , edgecolor='black')

'''
Seems to have an normaldisturbed time, with a symmetrical middlepoint
'''

mean  = dfb['time'].mean()
median = dfb['time'].median()
skew  = dfb['time'].skew()      # 0 ≈ symmetrisk, >0 högerskev, <0 vänsterskev
print(f"HistB, mean={mean:.2f}, median={median:.2f}, skew={skew:.3f}")
'''
if skew = 0, its symmertrical.
if skew > 0, its a right-skew
if skew < 0, its a left-skew
'''
      
#%% #C
'''
How is load distributed
Why does it matter
uniform, normal, exponential, weibull
'''
dfc[['load']].plot(title='C',kind='hist', bins=10 , edgecolor='black')

'''
Seems like the graph has right-skewed distribution, with a long tail extending towards higher loads.
'''

mean  = dfc['load'].mean()
median = dfc['load'].median()
skew  = dfc['load'].skew()      # 0 ≈ symmetrisk, >0 högerskev, <0 vänsterskev
print(f"HistC, mean={mean:.2f}, median={median:.2f}, skew={skew:.3f}")
'''
if skew = 0, its symmertrical.
if skew > 0, its a right-skew
if skew < 0, its a left-skew
'''
#%% #CTime
'''
How is time distributed
Why does it matter
uniform, normal, exponential, weibull
'''
dfc[['time']].plot(title='C', kind='hist', bins=10 , edgecolor='black')

'''
Seems to have an normaldisturbed time, with a symmetrical middlepoint
'''

mean  = dfc['time'].mean()
median = dfc['time'].median()
skew  = dfc['time'].skew()      # 0 ≈ symmetrisk, >0 högerskev, <0 vänsterskev
print(f"HistC, mean={mean:.2f}, median={median:.2f}, skew={skew:.3f}")
'''
if skew = 0, its symmertrical.
if skew > 0, its a right-skew
if skew < 0, its a left-skew
'''

# %%


#%%
'''
variance = is the squared average point on how the points are spread around the mean.

standard deviation = the typical distance for a datapoint from the mean.

What is the meaning of 6sigma = means that 99.99966% of all the points, is within the =- 6sigma bandwidth, and those who are not are deviating from the rest and would mean that only 0.00034% of the product is not within the acceptence width. This with other words mean it has a very low defect rate.
'''
print("A")
print("Variance: ", dfa['load'].var(ddof=0))
print("Standard deviation: ", dfa['load'].std(ddof=0))

print("B")
print("Variance: ", dfb['load'].var(ddof=0))
print("Standard deviation: ", dfb['load'].std(ddof=0))

print("C")
print("Variance: ", dfc['load'].var(ddof=0))
print("Standard deviation: ", dfc['load'].std(ddof=0))


#%%
'''
Other plots that can be useful 
boxplot
'''


