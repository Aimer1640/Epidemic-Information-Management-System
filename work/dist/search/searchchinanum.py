import openpyxl
import requests

send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}

url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
session = requests.session()
response = requests.get(url, verify=False)
json_data = response.json()['data']
china_data = json_data['diseaseh5Shelf']['areaTree'][0]['children']  # 列表
data_set = []
bg = openpyxl.Workbook()
catch = bg.active
catch.title = "国内疫情实时数据"
catch.append(['省份', '新增确诊', '累计确诊', '现有确诊', '累计死亡', '治愈'])
for i in china_data:
    data_list = [i['name'], i['today']['confirm'], i['total']['confirm'], i['total']['nowConfirm'], i['total']['dead'],
                 i['total']['heal']]
    for j in range(len(data_list)):
        if data_list[j] == '':
            data_list[j] = '0'
    catch.append(data_list)
bg.save('../data.xlsx')
