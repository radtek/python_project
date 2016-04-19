'''
写着玩玩的~
Created on 2016年3月28日
@author: Songge
''' 
import os

def hw(n):
    if n==1:
        return 1
    else:
        return 2**n
    
print(hw(3));
print('系统CPU数量：',os.cpu_count());
print('当前登陆用户：',os.getlogin());
