# coding=utf-8
import unittest
import requests
import ddt

@ddt.ddt
class MyTestCase(unittest.TestCase):
    @ddt.data("10","1")
    #@ddt.unpack
    def testGet(self,pagesize):
        #header部分的配置
        headers = {
        'User - Agent':'56konapp-3.5.8Dalvik/1.6.0(Linux;U;Android4.3;HTCEvo4GLTE-4.3-API18-720x1280Build/JLS36G)000000000000000',
        'Host':'api.56come.cn',
        'Connection':'Keep-Alive',
        'Accept-Encoding':'gzip'
        }

        #cookie部分的配置

        #get请求的构造
        res = requests.get('http://api.56come.cn/task/fav-list?pagesize='+pagesize+'&m=1'
                           '&page=1&sort_desc=desc&sort_by=updated_at&status=10&access_token=W2eGVX5svTYFvDkMk2Rsd3qaEJvUyFkOWo394wlI&',
                           headers=headers)

        print(res.text)
        print(res.status_code)

        #验证
        self.assertTrue(u'01228gr货物028（aaaa）' in res.text)



if __name__ == '__main__':
    unittest.main()
