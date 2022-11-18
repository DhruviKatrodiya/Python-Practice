# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 22:52:56 2022

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

automobile=pd.read_csv('Automobile_data.csv')
print(automobile.head())

###gettingdatatypes
print(automobile.dtypes)

#gettingstatistics
print(automobile.describe())

#cleaningdata
print(automobile.isnull().sum())

###cleaningthenormalizeddata
###Findoutnumberofrecordshaving'?'valuefornormalizedlosses
print(automobile['normalized-losses'].loc[automobile['normalized-losses']=='?'].count())

###settingmissingtomean
###Settingthemissingvaluetomeanofnormalizedlossesandconverthe
# datatypetointegernl=automobile['normalized-losses'].loc[automobile['normalized-losses']!='?']nlmean=nl.astype(str).astype(int).mean()automobile['normalized-losses']=automobile['normalized-losses'].replace('?',nlmean).astype(int)
# print(automobile['normalized-losses'].head())

##cleaningpricedata
##Findoutthenumberofvalueswhicharenotnumeric
print(automobile['price'].str.isnumeric().value_counts())
##Listoutthevalueswhicharenotnumeric
print(automobile['price'].loc[automobile['price'].str.isnumeric()==False])

##Settingthemissingvaluetomeanofpriceandconvertthedatatypeto
# integerprice=automobile['price'].loc[automobile['price']!='?']pmean=price.astype(str).astype(int).mean()automobile['price']=automobile['price'].replace('?',pmean).astype(int)
# print(automobile['price'].head())


# automobile.symboling.hist(bins=6,color='green')
# plt.title("Insuranceriskratingsofvehicles")
# plt.ylabel('Numberofvehicles')
# plt.xlabel('Risk rating')