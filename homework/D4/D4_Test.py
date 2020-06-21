
import os

import numpy as np
import pandas as pd

dir_data = 'D:\\Python Data\\ML100Days\\ML100DAYS\\homework\\D4\\'

f_app = os.path.join(dir_data, 'application_train.csv')
print('Path of read in data: %s' % (f_app))
app_train = pd.read_csv(f_app)
#print(app_train)
#?pd.read_csv
data=app_train
print(data.head())
print(data.info())

print("---"+"資料的 row 數以及 column 數")
#資料的 row 數以及 column 數
df = pd.DataFrame(app_train) 
print(df.shape[1],df.shape[0],len(df))

print("---"+"列出所有欄位")
#列出所有欄位
print(df.columns)

#截取部分資料
data2=data.loc[5:10][['SK_ID_CURR','FLAG_OWN_REALTY','CNT_CHILDREN']]
print(data2)
#describe主要是看資料的平均值、分佈情況、是否有資料傾斜Skew的問題
print(df.describe)

#將資料讀入 series 方法中
select_df = pd.DataFrame(app_train) 
print("---"+"有遺失值的觀測值都刪除")
# 有遺失值的觀測值都刪除
drop_value = select_df.dropna() 
print(drop_value)  
print("---"+"有遺失值的觀測值填補 0")  
# 有遺失值的觀測值填補 0  
filled_value = select_df.fillna(0) 
print(filled_value)  
print("---"+"依欄位填補遺失值")  
# 依欄位填補遺失值  
filled_value_column = select_df.fillna({"shop name": "NULL", "maket size": 0}) 
print(filled_value_column) 


#Pandas主要有兩大資料結構：
  #Series 欄位(一維度)
  #DataFrame 表格（二維度）