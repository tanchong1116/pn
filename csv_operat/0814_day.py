#:/user/bin/env python

#author:tanchong


import requests
import csv


url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
def get_Headers():
	headers={
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
	    'Referer': 'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
	    'Cookie': 'JSESSIONID=ABAAABAABEEAAJA2AEF10F20EE11BCB8E92B124D6654CD2; WEBTJ-ID=20190814175717-16c8f8f6d9149b-0d3e385ee497e8-784a5935-1882041-16c8f8f6d92382; TG-TRACK-CODE=index_search; SEARCH_ID=33c6c538784d4acda7fa4752c1d6db99; X_HTTP_TOKEN=debf130872c9febb6666775651976d5a2d625c8975; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565776667; LGRID=20190814175746-f79bccd2-be79-11e9-89c2-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565776638; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190814175717-e617dee3-be79-11e9-a500-5254005c3644; PRE_SITE=; LGSID=20190814175717-e617dc37-be79-11e9-a500-5254005c3644; user_trace_token=20190814175717-e617da99-be79-11e9-a500-5254005c3644; _gat=1; _gid=GA1.2.377804358.1565776638; _ga=GA1.2.929755187.1565776638; PRE_HOST=; PRE_UTM=; index_location_city=%E5%85%A8%E5%9B%BD',
	    }
	return headers

# def get_all():
# 	for i in range(1,31):
# 		pass
# 	return i

def lagou(page):
	positions=[]
	r=requests.post(
		url=url,
	    headers=get_Headers(),
	    data={'first':False,'pn':page,'kd':'自动化测试工程师','sid':'615d63e991134191b24d32eb43e1b327'})

	for i in range(15):
		city = r.json()['content']['positionResult']['result'][i]['city']
		education = r.json()['content']['positionResult']['result'][i]['education']
		workYear = r.json()['content']['positionResult']['result'][i]['workYear']
		positionAdvantage = r.json()['content']['positionResult']['result'][i]['positionAdvantage']
		salary = r.json()['content']['positionResult']['result'][i]['salary']
		companyFullName = r.json()['content']['positionResult']['result'][i]['companyFullName']
		positionLables = r.json()['content']['positionResult']['result'][i]['positionLables']
		position = {
			'公司名称': companyFullName,
			'城市': city,
			'学历': education,
			'工作年限': workYear,
			'薪资': salary,
			'工作标签': positionLables,
			'福利': positionAdvantage
		}
		positions.append(position)

	return positions

def csvWrite():
	headers={'公司名称','城市','薪资','工作年限','学历','福利','工作标签'}
	for item in range(1,31):
		positions=lagou(page=item)
		with open('lagou.csv','a',newline='',encoding='gbk') as f:
			writer=csv.DictWriter(f,headers)
			writer.writeheader()
			writer.writerows(positions)

csvWrite()