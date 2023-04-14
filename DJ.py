import random
import os
aa = 0
while aa < 1:
    print('=============================')
    print('第一层')
    a = random.randint(0,1)
    if a == 0:
        zidong = '自动运输的位置是4,智慧港口的位置为5'
    else:
        zidong = '自动运输的位置是5,智慧港口的位置为4'
    b = random.randint(0,1)
    if b == 0:
        zidongfx = '自动运输方向为1'
    else:
        zidongfx = '自动运输方向为2'
    c = random.randint(0,1)
    if c == 0:
        zhihuifx = '智慧港口方向为1'
    else:
        zhihuifx = '智慧港口方向为2'
    print(zidong+','+zidongfx+','+zhihuifx)
    num1 = [1,6,7,8,9,10]                       #定义四个任务位置的列表
    #第一次随机位置开始
    wz1 = random.sample(num1,1)                 #随机出来一个位置，目前是列表形态
    weizhi1 = str(wz1[0])                       #赋值给weizhi1，方便输出
    print('收集大数据的位置是：'+weizhi1)
    num1.remove(int(weizhi1))                   #删除掉这个位置的可能性
    #第一次终结
    wz1 = random.sample(num1,1)
    weizhi1 = str(wz1[0])
    print('切换5G的位置是：'+weizhi1)
    num1.remove(int(weizhi1))
    #第二次终结
    wz1 = random.sample(num1,1)
    weizhi1 = str(wz1[0])
    print('信息上传的位置是：'+weizhi1)
    num1.remove(int(weizhi1))
    #第三次终结
    wz1 = random.sample(num1,1)
    weizhi1 = str(wz1[0])
    print('无线传输的位置是：'+weizhi1)
    num1.remove(int(weizhi1))
    #第四次终结，完成
    #随机图像识别的位置
    a = random.randint(0,1)
    if a == 0:
        print('图像识别的位置是2,物品定位的位置为3')
    else:
        print('图像识别的位置是3,物品定位的位置为2')
    print('----------------------------------------------------------')
    print('第二层')
    # num2 = [1,2,3,4]        #信息处理的方向
    # xinxi = str(random.sample(num2,1)[0])      #随机一个数出来
    print('信息处理的方向是：1')
    num3 = [11,13,15,17]        #信息编码的位置
    bianma = str(random.sample(num3,1)[0])      #随机一个数出来
    print('信息编码的位置是：'+bianma)

    a = random.randint(0,1)
    if a == 0:
        print('订单处理的位置是12,扫描二维码的位置为18')
    else:
        print('订单处理的位置是18,扫描二维码的位置为12')

    a = random.randint(0,1)
    if a == 0:
        print('文字识别的位置是14,下载数据的位置是16')
    else:
        print('文字识别的位置是16,下载数据的位置是14')
    print('===========================================')
    zhusun = input('按回车重新随机')

   # os.system('pause')         目前不可用
