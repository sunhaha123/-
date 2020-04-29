# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:31:51 2020

@author: sunjh
"""

import numpy as np

#变量
#墙壁距离泳池的距离
#d1=2
#拍摄泳道的宽度
#d2=10.66
#需要拍摄泳道的长度
#l1=15
#摄像头高度
#h1=4
#需要覆盖的泳池长度
#e=15

def cal(d1,d2,h1,e):
#视频拍摄中心点到摄像头墙壁所在的距离
    sum_d=d1+d2
    #摄像头距离中心点的直线距离
    c_d=np.sqrt(sum_d*sum_d+h1*h1)
    #镜头视角度数
    degree=(np.arctan((e/2)/c_d))/np.pi*180
    return c_d,2*degree

if __name__=="__main__":
    print("摄像头视角度数:%d"%cal(d1=1,d2=5.33,h1=4,e=15)[1])
    c_d,degree=cal(d1=1.5,d2=5.33,h1=4,e=15)
    if degree>95:
        print('焦距为：2.8mm')
        half_length=c_d*np.tan(95/2/180*np.pi) 
        print('镜头安装位置(距离泳池边的距离)：%d'%half_length) 
    elif degree>86:
        print('焦距为4mm')
        half_length=c_d*np.tan(86/2/180*np.pi) 
        print('镜头安装位置(距离泳池边的距离)：%d'%half_length) 
    elif degree>54.5:
        print('焦距为6mm')
        half_length=c_d*np.tan(54.5/2/180*np.pi) 
        print('镜头安装位置(距离泳池边的距离)：%d'%half_length) 
    elif degree > 43:
        print('焦距为8mm')
        half_length=c_d*np.tan(43/2/180*np.pi) 
        print('镜头安装位置(距离泳池边的距离)：%d'%half_length) 
    else:
        print('焦距为12mm')
        half_length=c_d*np.tan(90/2/180*np.pi) 
        print('镜头安装位置(距离泳池边的距离)：%d'%half_length) 
        
       
        
        
        
    