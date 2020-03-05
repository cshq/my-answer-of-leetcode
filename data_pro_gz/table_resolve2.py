# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:58:03 2020

@author: THTF
"""
import numpy as np
import pandas as pd
def pdt_auth(data_adr):
    df=pd.read_excel(data_adr,sheet_name=0)
    re=[]
    for i in range(len(df)):
        for j in range(7,len(df.loc[0])):
            if not df.isnull().loc[i][j]:
                re.append(df.columns[j])
    re=pd.DataFrame(re,columns=['产品权限'])
    kz=pd.DataFrame()
    for i in range(len(df)):
        for j in range(7,len(df.loc[0])):
            if not df.isnull().loc[i][j]:
                kz=kz.append(df.iloc[i,[0,2,3,4]])
    index=pd.Index(np.arange(len(kz)))
    kz.index=index
    res=pd.merge(kz,re,left_index=True,right_index=True)
    res.to_excel('C:\\Users\\THTF\\Desktop\\jx_sh2_res.xlsx')
    return 
    
    
    
if __name__=='__main__':
    pdt_auth('C:/Users/THTF/Desktop/jx_sh2.xlsx')
    
    