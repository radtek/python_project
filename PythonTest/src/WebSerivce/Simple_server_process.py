'''
此类用来编写服务的实际业务
Created on 2016年4月5日
@author: Songge
'''

from ctypes import *
from GetSystemInfo import *
import base64
'''
用来测试调用系统user32.dll的例子
user32 = windll.LoadLibrary('user32.dll')
user32.MessageBoxA(0,b'it is ok!',b'Ctypes load user32.dll',1)
'''


#主方法
def processMain(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    
    #请求方法
    s_method = environ['REQUEST_METHOD']
    #调用应用路径
    s_path = environ['PATH_INFO']
    
    print('Servr path is ',s_path)
    
    if s_method=='GET' and s_path=='/Prs':

        s_carddll = getCardDllName()        
        #加载外部DLL
        idCard = windll.LoadLibrary(s_carddll)         
        
        ret = idCard.SDT_OpenPort(1001)
        print('打开读卡器端口:',ret)
        pucManaInfo = pointer(c_ubyte(0))
        ret = idCard.SDT_StartFindIDCard(1001, pucManaInfo, 0)
        print('查找卡片：',ret)
        ret = idCard.SDT_SelectIDCard(1001, pucManaInfo, 0);
        print('选择卡片：',ret)
        #读取身份证信息和相片信息
        byte_type = c_ubyte*256
        pucCHMsg = byte_type()
        
        puiCHMsgLen = pointer(c_uint(256))

        byte2_type = c_ubyte*1024
        pucPHMsg = byte2_type()
        
        puiPHMsgLen = pointer(c_uint(1024))
        
        #读卡内信息
        i_ret = idCard.SDT_ReadBaseMsg(1001,pucCHMsg,puiCHMsgLen,pucPHMsg,puiPHMsgLen,0)        
        if i_ret != 0x90:
            print('读取身份证机读文字信息和相片信息失败，返回值为:',i_ret) 
            idCard.SDT_Close(1001)
        else:
            #文字信息
            s_mess = Byte2Unicode(pucCHMsg)            
        print(s_mess)
        
        print('姓名：',s_mess[0:15].strip())
        s_html =  '<h1/>姓名：'+s_mess[0:15].strip() +'<br>'
        print('身份证短码：',s_mess[15:26].strip())
        s_html += '<h1/>身份证短码：'+ s_mess[15:26].strip()+'<br>'
        print('地址：',s_mess[26:61].strip())
        s_html += '<h1/>地址：' + s_mess[26:61].strip()+'<br>'
        print('身份证号：',s_mess[61:79].strip())
        s_html += '<h1/>身份证号：' + s_mess[61:79].strip()+'<br>'
        print('发证公安局：',s_mess[79:94].strip())
        s_html += '<h1/>发证公安局：'+ s_mess[79:94].strip()+'<br>'
        print('发证日期：',s_mess[94:len(s_mess)].strip())
        s_html += '<h1/>发证日期：'+s_mess[94:len(s_mess)].strip()+'<br>'
        #图片
        #p_PhMsg = base64.b64encode(pucPHMsg)
        #print('卡图片：',p_PhMsg.decode('ascii'))
        #将图片写入文件
        fh = open("photo.wlt", "wb")
        fh.write(pucPHMsg)
        fh.close()
        
        s_photodll = 'WltRS.dll'
        photodll =  windll.LoadLibrary(s_photodll) 
        ret = photodll.GetBmp("photo.wlt", 2);
        print(ret)
        
        #将身份证文件取出存入文件中（主要用来处理像片）
        #i_ret = idCard.SDT_ReadBaseMsgToFile(1001,c_text,puiCHMsgLen,c_photo,puiPHMsgLen)
        
        #打开图片，查看字符串
        #with open("photo.bmp", "rb") as imageFile:
        #    str = base64.b64encode(imageFile.read())
        #    print('外部图片：',str)        
        
        print(puiCHMsgLen.contents.value)
        print(puiPHMsgLen.contents.value)

         
        return [s_html.encode('GBK')]
    else:
        return ['<h1>请输入正确的访问路径!</h1>'.encode('GBK')]

    
#字符转换函数
def Byte2Unicode(abytes,bStart=0,bEnd=0):
    #返回值
    sret = ''
    if bEnd==0:
        bEnd=len(abytes)
    
    j = bStart
    
    while j<bEnd :        
        #低位处理
        lw = abytes[j]
        j = j+1;
        if lw < 0 :
            lw = lw + 256;
        #高位处理
        hi = abytes[j]
        j = j+1;
        if hi < 0 :
            hi = hi + 256;
        iall = lw + (hi<<8)
        #拼接字节
        sret = sret + chr(iall)
    return sret
            

