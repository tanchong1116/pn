#:/user/bin/env python

#author:tanchong

import unittest
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
	# 下面的1，2，3代表我们传入的参数，每次传入一个值
	@data(1,2,3)
	# 定义一个value来接收传入的参数
	def test_add(self,value):
		# 断言value值是否等于2
		self.assertEqual(value,2)

if __name__=='__main__':
	unittest.main()