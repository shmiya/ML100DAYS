# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 23:46:07 2020

@author: shmiy
"""
import numpy as np
import matplotlib.pyplot as plt

w = 3
b = 0.5
x_lin = np.linspace(0, 100, 101)
y = (x_lin + np.random.randn(101) * 5) * w + b
#----------------------------------------------------
 #plt.plot(x_lin, y, 'b.', label = 'data points')
 #plt.title("Assume we have data points")
 #plt.legend(loc = 2)
 #plt.show()
#-----------------------------------------------------    
y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
#上面的 'b.' 是藍色點狀, 下面的 'r-' 是紅色線狀, label 是圖示上的名稱
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)  #圖標位置
plt.show()
#-----------------------------------------------------  
#平均絕對誤差（Mean Absolute Error）
#對同一物理量進行多次測量時，各次測量值及其絕對誤差不會相同，
#我們將各次測量的絕對誤差取絕對值後再求平均值，並稱其為平均絕對誤差。
#平均絕對誤差是所有單個觀測值與算術平均值的偏差的絕對值的平均。
#與平均誤差相比，平均絕對誤差由於離差被絕對值化，不會出現正負相抵消的情況，
#因而，平均絕對誤差能更好地反映預測值誤差的實際情況。
#MAE : 將兩個陣列相減後, 取絕對值(abs), 再將整個陣列加總成一個數字(sum), 最後除以y的長度(len)
def mean_absolute_error(y, yp):  
    mae =  sum(abs(y - yp)) / len(y) 
    #print(mae)
    return mae

#-----------------------------------------------------       
MAE = mean_absolute_error(y, y_hat)
print("The Mean absolute error is =%.3f" %(MAE))      
#-----------------------------------------------------
#均方誤差（Mean-Square Error, MSE）
#指參數估計值與參數真值之差平方的期望值，記為 MSE。MSE 是衡量「平均誤差」的一種較方便的方法，
#MSE 可以評價資料的變化程度，MSE 的值越小，說明預測模型描述實驗資料具有更好的精確度。
#
def Mean_Square_Error(y,yp):
     mse= sum(np.square(y-yp))/len(y)
     return mse

MSE=Mean_Square_Error(y,y_hat)
print("The Mean Square error is =%.3f" %(MSE))

    
    
    
    
    