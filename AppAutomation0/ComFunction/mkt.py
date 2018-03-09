#-*- coding: utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner import MonkeyImage
import time
 
 
def wake_device():
    device.wake()   #  唤醒设备
    MonkeyRunner.sleep(1.0)
    device.drag((170,520), (400,520), 0.5, 10)  # 模拟拖动，从点1到点2，时间0.5秒，中间插入10个点。解锁
 
def start_bwzq():
    device.startActivity(component="com.hummingbird.zhaoqin.kkk5/com.hummingbird.zhaoqin.kkk5.MainActivity")  # 启动 bwzq
 
def take_snapshot():
    result = device.takeSnapshot()   #截图
    result.writeToFile('G:/AppAutomation/AndroidAppAutomation/SnapShot/ExpectPageShot/shot2.png','png')
 
def assert_pic(src_pic):
    imageA = MonkeyRunner.loadImageFromFile(src_pic,'png')
    MonkeyRunner.sleep(1)
    image=device.takeSnapshot()
    MonkeyRunner.sleep(1)
#     tag = image.sameAs(imageA, 0.95)
    tag = image.sameAs(imageA, 0.70)
#     print tag
#     log = open('D:/workspace/testbwzq/src_images/mkt_log.txt', 'a')    # 记日志
# #     log_tm = device.shell('date +%Y%m%d%H%M%S')
#     log_tm = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#     if tag:
#         log.write(log_tm + "|: PASS\n")
# #         MonkeyRunner.alert('pass', 'test', u'确定')
#     else:
#         log.write(log_tm + "|: Fail,please check\n")
# #         MonkeyRunner.alert('fail', 'test', u'确定')
#     log.close()
    return tag
 
def WaitforelementPresent(Value, count = 8, element_bak = ''):
    isPresent = assert_pic(Value)
    if not isPresent:
        print str(isPresent) + "\t" + Value
#         n = 1
        for i in range(1, count, 1):
            print "wait 2s ..."
            time.sleep(2) # 等待时间固定模式
            isPresent = assert_pic(Value)
            if isPresent:
                break
            if i > 6:
#                 if str(element_bak) != '':
# #                         self.element_bak_isPresent = str(self.driver.find_element_by_id(self.element_bak).is_displayed())    # error
#                     element_bak_isPresent = assert_pic(element_bak)
#                     print str(element_bak_isPresent) + "\t" + element_bak
#                     if element_bak_isPresent:
# #                         self.driver.find_element_by_id(self.element_bak).click()
#                         print "click " + element_bak + " " + str(n) +" time(s)"
#                         n += 1
#                     start_bwzq()
                    MonkeyRunner.alert(u'页面异常', 'fail', u'确定')
                    break
#     element_bak = Value
    print str(isPresent) + "\t" + Value
    return isPresent
 
def pic_assert_or_not():
    take_snapshot()
    MonkeyRunner.sleep(3)
    WaitforelementPresent('D:/workspace/testbwzq/src_images/shot1.png')

def chk_argv():
    pass


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        if sys.argv[1].isdigit():
            tmp = int(sys.argv[1])
            if tmp > 1 and tmp < 65:
                n = tmp
                print 'n=' + str(n)
            else:
                print('start_id: 2-64')
                sys.exit(0)
        else:
            print('start_id: int')
            sys.exit(0)
        if sys.argv[2].isdigit():
            tmp2 = int(sys.argv[2])
            if tmp2 >= tmp and tmp2 < 65:
                end = tmp2
                print 'end='+ str(end)
            else:
                print('end_id: >start_id & 2-64')
                sys.exit(0)
        else:
            print('end_id: int')
            sys.exit(0)
    else:
        print('usage:')
        print('\tmkt.py [start_id] [end_id]')
        print('\tstart_id: 2-64')
        print('\tend_id: 2-64')
        sys.exit(0)

#     wake_device()
    device = MonkeyRunner.waitForConnection()
    print 'connected'
    MonkeyRunner.sleep(1)
    start_bwzq()
    MonkeyRunner.sleep(3)
 
#     n = 44
#     end = 45
    for login_count in range(n, end+1, 1):
        print '>>>>>>>>>>>>>>>>>>>> No. ' + str(login_count) + ' >>>>>>>>>>>>>>>>>>>>'
        WaitforelementPresent('D:/workspace/testbwzq/src_images/pic101_login.png')
        device.drag((360,358), (365,360), 1, 3)
        MonkeyRunner.sleep(1)
        for i in range(1, 11, 1):
    #         device.press('KEYCODE_FORWARD_DEL', MonkeyDevice.DOWN_AND_UP)   # 向前删除字符，光标右边的字符
            device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)   # 向后删除字符，光标左边的字符
        if n<10:
            device.type('kkk523100')    # 向编辑区域输入文本
        else:
            device.type('kkk52310')
        device.type(str(n))
        MonkeyRunner.sleep(1)
        device.takeSnapshot().writeToFile('D:/workspace/testbwzq/src_images/' + str(n) + '_login_' + time.strftime('%Y%m%d_%H%M%S',time.localtime()) + '.png','png')
#         MonkeyRunner.sleep(1)
        device.drag((130,576), (133,578), 0.5, 2)  # 点击快速登录
#         MonkeyRunner.sleep(1)
 
        WaitforelementPresent('D:/workspace/testbwzq/src_images/pic102_login_click2login.png')
        device.drag((240,605), (243,608), 0.5, 2)  # 点击进入游戏
        MonkeyRunner.sleep(1)
        device.takeSnapshot().writeToFile('D:/workspace/testbwzq/src_images/' + str(n) + '_login_' + time.strftime('%Y%m%d_%H%M%S',time.localtime()) + '.png','png')
 
        n+=1
 
        WaitforelementPresent('D:/workspace/testbwzq/src_images/pic103_gonggao_guanbi.png')
        device.drag((233,678), (236,680), 0.5, 2)  # 关闭公告
        MonkeyRunner.sleep(1)
        device.takeSnapshot().writeToFile('D:/workspace/testbwzq/src_images/' + str(n-1) + '_login_' + time.strftime('%Y%m%d_%H%M%S',time.localtime()) + '.png','png')
 
        WaitforelementPresent('D:/workspace/testbwzq/src_images/pic104_shouye_shangwu.png')
        device.drag((434,658), (430,654), 0.5, 2)  # 点击首页-更多
#         MonkeyRunner.sleep(1)
 
        WaitforelementPresent('D:/workspace/testbwzq/src_images/pic105_shouye_gengduo.png')
        device.drag((100,573), (102,575), 0.5, 2)  # 点击首页-更多-系统
#         MonkeyRunner.sleep(1)
 
        WaitforelementPresent('D:/workspace/testbwzq/src_images/pic106_xitong.png')
        device.drag((347,509), (350,512), 0.5, 2)  # 点击首页-更多-系统-切换账号
#         MonkeyRunner.sleep(1)
 
        WaitforelementPresent('D:/workspace/testbwzq/src_images/pic107_qiehuanzhanghao_queding.png')
        device.drag((159,486), (162,490), 0.5, 2)  # 点击首页-更多-系统-切换账号-确定
        MonkeyRunner.sleep(1)

#     assert_pic('D:/workspace/testbwzq/src_images/pic101_login.png')

#     pic_assert_or_not()
#     take_snapshot()
#     WaitforelementPresent('D:/workspace/testbwzq/src_images/shot1.png')

#     get_Accessibility_Ids()
    