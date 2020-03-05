# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:02:24 2020

@author: THTF
"""

import numpy as np
import pandas as pd
def pdt_spi(data_adr):
    df=pd.read_excel(data_adr,sheet_name=27)
    res=[]
    for i in df['产品权限']:
        res.extend((i.split('、')))
    df_res=pd.DataFrame(res,columns=['产品权限'])
    ppq=pd.DataFrame()
    for i in range(len(df)):
        ppq=ppq.append(df.iloc[i,[0,1,2,3,5,6]])
        for j in df.loc[i][4]:
            if j=='、':
                ppq=ppq.append(df.iloc[i,[0,1,2,3,5,6]])
    index=pd.Index(np.arange(len(ppq)))
    ppq.index=index
    mmm=pd.merge(ppq,df_res,left_index=True,right_index=True)
    mmm=mmm.iloc[:,[0,1,4,5,6,2,3]].iloc[:,[0,3,6,2,4,1,5]]
    mmm.to_excel('C:\\Users\\THTF\\Desktop\\qxwjj\\陕西.xlsx')
    return

if __name__=='__main__':
    pdt_spi('C:/Users/THTF/Desktop/qxhz.xlsx')