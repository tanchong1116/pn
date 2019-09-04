#:/user/bin/env python

#author:tanchong

import os
import sys

# 获取当前文件家路径
print(os.path.dirname(__file__))

# 获取当前路径的上一个路径
print(os.path.dirname(os.path.dirname(__file__)))

# 创建一个文件夹mkdir
# os.mkdir('c:/log')

# 删除一个文件夹
# os.rmdir('c:/log')

# 对文件夹的重命名rename
# os.rename('c:/log','c:/newlog')

# 读取文件内容
base_dir=os.path.dirname(__file__)
f=open('log.text','r')
print(f.read())