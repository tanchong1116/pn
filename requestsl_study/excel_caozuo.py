#:/user/bin/env python

#author:tanchong

import xlrd
import os
from xlutils.copy import copy

def base_dir(filename=None):
	return os.path.join(os.path.dirname(__file__),filename)


'''excel文件的读取'''
# work=xlrd.open_workbook(base_dir('data.xls'))
# # 获取到第一个sheet
# sheet=work.sheet_by_index(0)
# # 查看多少行
# print(sheet.nrows)
# # 获取单元格的内容
# print(sheet.cell_value(8,1))

'''对excel文件内容的修改'''
work=xlrd.open_workbook(base_dir('data.xls'))
old_content=copy(work)
ws=old_content.get_sheet(0)
ws.write(9,2,'无涯社区')
old_content.save(base_dir('data.xls'))