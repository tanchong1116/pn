#:/user/bin/env python

#author:tanchong

import pymysql

def connMySql():
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
		cur=conn.cursor()
		# 查询单个语句
		# sql='select * from flood_contacts where ContactsId=%s'
		# params=('1014710676716916736',)  元组中只有1个数据时，数据后面要有逗号
		# cur.execute(sql,params)
		# data=cur.fetchone()
		# 批量查询
		cur.execute('select * from flood_contacts')
		data=cur.fetchall()
		# for item in data:
		# 	print(item)
		# 列表推导式:将数据转换成列表类型
		db=[item for item in data]
		print(db)
	finally:
		cur.close()
		conn.close()
print(connMySql())
