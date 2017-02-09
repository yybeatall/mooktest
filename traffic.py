#/usr/bin/python
#encoding:utf-8
import csv
import os
import string
import time
import subprocess

#控制类
class Controller(object):
    def __init__(self, count):
        #定义测试的次数
        self.counter = count
        #定义收集数据的数组
        self.alldata = [("timestamp", "traffic")]
        self.result = ""

    #单次测试过程
    def testprocess(self):
        #执行获取进程的命令
        #【】改动 这里一定要设置成global，不明白啊
        global receive1, transmit1, receive2, transmit2
        result = str(subprocess.check_output("adb shell ps | grep com.yihu001.kon.driver"))
        #获取进程ID
        print(result)
        pid = result.split()[1]
        print(pid)
        #【】获取进程ID使用的流量，这里还有点问题，这样去到的并不是这个packge的id，也有可能是相关的
        traffic = str(subprocess.check_output("adb shell cat /proc/"+pid+"/net/dev"))
        print(traffic)
        #【】改动
        receive = traffic.split('\\r\\r\\n')
        for line in receive:
            if "eth0" in line:
                #将所有空行换成#
                #【】
                line = "#".join(line.split())
                #按#号拆分,获取收到和发出的流量
                receive1 = line.split("#")[1]
                transmit1 = line.split("#")[9]
                print (receive1)
                print (transmit1)
            elif "eth1" in line:
                # 将所有空行换成#
                #【】
                line =  "#".join(line.split())
                # 按#号拆分,获取收到和发出的流量
                receive2 = line.split("#")[1]
                transmit2 = line.split("#")[9]
                print (receive2)
                print (transmit2)
        #计算所有流量的之和
        alltraffic = int(receive1)+int(transmit1)+int(receive2)+int(transmit2)
        #alltraffic = 100000
        #按KB计算流量值
        alltraffic = alltraffic/1024
        #获取当前时间
        currenttime = self.getCurrentTime()
        #将获取到的数据存到数组中
        self.alldata.append((currenttime, alltraffic))

    #多次测试过程控制
    def run(self):
        while self.counter >0:
            self.testprocess()
            self.counter = self.counter - 1
            #每5秒钟采集一次数据
            time.sleep(5)

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    #数据的存储
    def SaveDataToCSV(self):
        #【】
        csvfile = open('traffic.csv', 'w',newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(2)
    controller.run()
    controller.SaveDataToCSV()