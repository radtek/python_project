'''
Created on 2016年4月6日

@author: Songge
'''

import platform
import os

def getPlatform():
    print("----------Operation System--------------------------")
    print('System:',platform.system())
    print('Arch:',platform.architecture())
    print('Platform:',platform.platform())
    print('CPU数量：',os.cpu_count());
    print('登陆用户：',os.getlogin());
    
    print ("--------------Python Version-------------------------")
    print('Python:',platform.python_version())
    
    
def is64Windows():
    b_64bit = '64bit' in platform.architecture()
    b_win = 'Win' in platform.platform()
    return b_64bit and b_win

def getCardDllName():
    if is64Windows():
        return 'sdtapi_x64.dll' 
    else:
        return 'sdtapi.dll' 