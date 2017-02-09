#/usr/bin/python
#encoding:utf-8
import csv
import os
import time
import subprocess

#控制类


class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.alldata = [("timestamp", "cpustatus")]

    #单次测试过程
    def testprocess(self):
        result = subprocess.check_output("adb shell dumpsys cpuinfo | grep com.yihu001.kon.driver")
        print(result)
        result = str(result)


        #for line in result.splitlines():
        cpuvalue = result.split("%")[0]
        cpuvalue = cpuvalue.split("b'  ")[1]
        print(cpuvalue)

        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime, cpuvalue))

    #多次执行测试过程
    def run(self):
        while self.counter >0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(3)

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = open('cpustatus.csv', 'w',newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(2)
    controller.run()
    controller.SaveDataToCSV()
