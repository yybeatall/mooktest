# coding=utf-8
import unittest
import requests
import ddt

@ddt.ddt

class MyTestCase(unittest.TestCase):
    @ddt.data(
        ("13940914602","123456"),
        ("13940914601", "12345"),
        ("###", "123456"),
        ("13940914601", " ")

    )
    @ddt.unpack
    def testPost(self,username,password):
        #header部分的配置
        headers = {
        'User - Agent':'56konapp-3.5.8 Dalvik/1.6.0 (Linux; U; Android 4.3; HTC Evo 4G LTE - 4.3 - API 18 - 720x1280 Build/JLS36G) 000000000000000',
        'Host':'api.56come.cn',
        'Connection':'Keep-Alive',
        'Accept-Encoding':'gzip',
        'Content-Length':'151'
        }

        #cookie部分的配置

        '''cookies = dict{

        }'''

        keyword = {
            'username':username,
            'device_brand':'unknown',
            'client_secret':'56konapp12qwaszx',
            'client_id':'56konapp',
            'getui_cid':'424aec0717875719272c2c74e9c3f905',
            'password':password
        }

        #get请求的构造
        res = requests.post('http://api.56come.cn/auth/signin',
                           headers=headers,
                            data=keyword)

        print(res.text)
        print(res.status_code)

        #验证
        self.assertTrue(u'username' in res.text)



if __name__ == '__main__':
    unittest.main()

