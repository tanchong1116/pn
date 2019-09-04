#:/user/bin/env python

#author:tanchong

# 往mysql中插入数据
import pymysql

def insertMySql():
	try:
		conn=pymysql.connect(
			host='192.168.0.232',
		    port=3306,
			user='root',
			passwd='admin123',
			db='dev')
	except Exception as e:
		return e.args
	else:
		cur = conn.cursor()
		# 插入单个数据
		sql='insert into flood_contacts values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		# 批量插入数据
		params=[
			('1014710676716916733', 0, '黄多1', '13565188332', '水利管理总站副站长', '红旗水库', 0, '2019-08-09 11:20:52', 932921333963165696, 'Aiolos', '2019-08-09 11:20:52', 123, 'yhb'),
			('1014710676716916739', 0, '黄多2', '13565188332', '水利管理总站副站长', '红旗水库', 0, '2019-08-09 11:20:52',
			 932921333963165696, 'Aiolos', '2019-08-09 11:20:52', 123, 'yhb'),
			('1014710676716916731', 0, '黄多3', '13565188332', '水利管理总站副站长', '红旗水库', 0, '2019-08-09 11:20:52',
			 932921333963165696, 'Aiolos', '2019-08-09 11:20:52', 123, 'yhb'),
			]
		# 插入多个数据时，使用executemany
		cur.executemany(sql,params)
		conn.commit()
	finally:
		cur.close()
		conn.close()


print(insertMySql())