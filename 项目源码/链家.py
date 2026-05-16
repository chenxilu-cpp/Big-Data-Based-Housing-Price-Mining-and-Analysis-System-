
# 导入数据请求模块 --> 第三方模块, 需要安装 pip install requests
import requests
# 导入解析数据模块 --> 第三方模块, 需要安装 pip install parsel
import parsel
# 导入csv模块
import csv

# 创建文件
f = open('data.csv', mode='w', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '小区',
    '区域',
    '售价',
    '单价',
    '户型',
    '面积',
    '朝向',
    '装修',
    '楼层',
    '年份',
    '建筑类型',
    '详情页',
])
csv_writer.writeheader()
"""
发送请求, 模拟浏览器 对于 url地址 发送请求
    - 模拟浏览器 < 请求头 headers >
"""
# 模拟浏览器
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
for page in range(1, 101):
        print(f'###########################正在采集{page}页内容###########################')
    # 请求网址/网站
        url = f'https://cs.lianjia.com/ershoufang/pg{page}/'
    # 发送请求
        response = requests.get(url=url, headers=headers)
        # <Response [200]> 响应对象 200 状态码 表示请求成功
        print(response)
        """
        获取数据, 获取网页源代码 <获取服务器返回响应数据>
        
        解析数据, 提取我们想要的数据内容
            解析方法:
                1. re: 对于字符串数据直接进行解析提取
                2. css: 根据标签属性提取数据内容
                3. xpath: 根据标签节点提取数据内容
        
        css: 根据标签属性提取数据内容
        """
        # 把获取到html字符串数据, 转成可解析对象
        selector = parsel.Selector(response.text)
        # 获取所有房源信息所在li标签
        lis = selector.css('.sellListContent li.clear')
        # for循环遍历
        for li in lis:
            """
            提取具体房源信息: 标题 / 价格 / 位置 / 户型...
            .title a --> 表示定位class类名为title下面a标签
            """
            title = li.css('.title a::text').get()  # 标题
            info_list = li.css('.positionInfo a::text').getall()
            area = info_list[0]  # 小区名字
            area_1 = info_list[1]  # 地区
            totalPrice = li.css('.totalPrice span::text').get()  # 售价
            unitPrice = li.css('.unitPrice span::text').get().replace('元/平', '').replace(',', '')  # 单价
            houseInfo = li.css('.houseInfo::text').get().split(' | ')  # 信息
            houseType = houseInfo[0]  # 户型
            houseArea = houseInfo[1].replace('平米', '')  # 面积
            houseFace = houseInfo[2]  # 朝向
            fitment = houseInfo[3]  # 装修
            fool = houseInfo[4] if len(houseInfo) > 4 else '1'

            if len(houseInfo) == 7 and '年' in houseInfo[5]:
                year = houseInfo[5].replace('年建', '')
            else:
                year = ''
            house = houseInfo[-1]  # 建筑类型
            href = li.css('.title a::attr(href)').get()  # 详情页
            dit = {
                '标题': title,
                '小区': area,
                '区域': area_1,
                '售价': totalPrice,
                '单价': unitPrice,
                '户型': houseType,
                '面积': houseArea,
                '朝向': houseFace,
                '装修': fitment,
                '楼层': fool,
                '年份': year,
                '建筑类型': house,
                '详情页': href,
            }
            csv_writer.writerow(dit)
            print(dit)
            # print(title, area, area_1, totalPrice, unitPrice, houseType, houseArea, houseFace, fitment, fool, year, house, href)
        # 请求网址/网站
        url = f'https://cs.lianjia.com/ershoufang/yuhua/pg{page}/'
        # 发送请求
        response = requests.get(url=url, headers=headers)
        # <Response [200]> 响应对象 200 状态码 表示请求成功
        print(response)
        """
        获取数据, 获取网页源代码 <获取服务器返回响应数据>
    
        解析数据, 提取我们想要的数据内容
            解析方法:
                1. re: 对于字符串数据直接进行解析提取
                2. css: 根据标签属性提取数据内容
                3. xpath: 根据标签节点提取数据内容
    
        css: 根据标签属性提取数据内容
        """
        # 把获取到html字符串数据, 转成可解析对象
        selector = parsel.Selector(response.text)
        # 获取所有房源信息所在li标签
        lis = selector.css('.sellListContent li.clear')
        # for循环遍历
        for li in lis:
            """
            提取具体房源信息: 标题 / 价格 / 位置 / 户型...
            .title a --> 表示定位class类名为title下面a标签
            """
            title = li.css('.title a::text').get()  # 标题
            info_list = li.css('.positionInfo a::text').getall()
            area = info_list[0]  # 小区名字
            area_1 = info_list[1]  # 地区
            totalPrice = li.css('.totalPrice span::text').get()  # 售价
            unitPrice = li.css('.unitPrice span::text').get().replace('元/平', '').replace(',', '')  # 单价
            houseInfo = li.css('.houseInfo::text').get().split(' | ')  # 信息
            houseType = houseInfo[0]  # 户型
            houseArea = houseInfo[1].replace('平米', '')  # 面积
            houseFace = houseInfo[2]  # 朝向
            fitment = houseInfo[3]  # 装修
            fool = houseInfo[4] if len(houseInfo) > 4 else '1'

            if len(houseInfo) == 7 and '年' in houseInfo[5]:
                year = houseInfo[5].replace('年建', '')
            else:
                year = ''
            house = houseInfo[-1]  # 建筑类型
            href = li.css('.title a::attr(href)').get()  # 详情页
            dit = {
                '标题': title,
                '小区': area,
                '区域': area_1,
                '售价': totalPrice,
                '单价': unitPrice,
                '户型': houseType,
                '面积': houseArea,
                '朝向': houseFace,
                '装修': fitment,
                '楼层': fool,
                '年份': year,
                '建筑类型': house,
                '详情页': href,
            }
            csv_writer.writerow(dit)
            print(dit)
            # print(title, area, area_1, totalPrice, unitPrice, houseType, houseArea, houseFace, fitment, fool, year, house, href)
        # 请求网址/网站
        url = f'https://cs.lianjia.com/ershoufang/yuelu/pg{page}/'
        # 发送请求
        response = requests.get(url=url, headers=headers)
        # <Response [200]> 响应对象 200 状态码 表示请求成功
        print(response)
        """
        获取数据, 获取网页源代码 <获取服务器返回响应数据>

        解析数据, 提取我们想要的数据内容
            解析方法:
                1. re: 对于字符串数据直接进行解析提取
                2. css: 根据标签属性提取数据内容
                3. xpath: 根据标签节点提取数据内容

        css: 根据标签属性提取数据内容
        """
        # 把获取到html字符串数据, 转成可解析对象
        selector = parsel.Selector(response.text)
        # 获取所有房源信息所在li标签
        lis = selector.css('.sellListContent li.clear')
        # for循环遍历
        for li in lis:
            """
            提取具体房源信息: 标题 / 价格 / 位置 / 户型...
            .title a --> 表示定位class类名为title下面a标签
            """
            title = li.css('.title a::text').get()  # 标题
            info_list = li.css('.positionInfo a::text').getall()
            area = info_list[0]  # 小区名字
            area_1 = info_list[1]  # 地区
            totalPrice = li.css('.totalPrice span::text').get()  # 售价
            unitPrice = li.css('.unitPrice span::text').get().replace('元/平', '').replace(',', '')  # 单价
            houseInfo = li.css('.houseInfo::text').get().split(' | ')  # 信息
            houseType = houseInfo[0]  # 户型
            houseArea = houseInfo[1].replace('平米', '')  # 面积
            houseFace = houseInfo[2]  # 朝向
            fitment = houseInfo[3]  # 装修
            fool = houseInfo[4] if len(houseInfo) > 4 else '1'

            if len(houseInfo) == 7 and '年' in houseInfo[5]:
                year = houseInfo[5].replace('年建', '')
            else:
                year = ''
            house = houseInfo[-1]  # 建筑类型
            href = li.css('.title a::attr(href)').get()  # 详情页
            dit = {
                '标题': title,
                '小区': area,
                '区域': area_1,
                '售价': totalPrice,
                '单价': unitPrice,
                '户型': houseType,
                '面积': houseArea,
                '朝向': houseFace,
                '装修': fitment,
                '楼层': fool,
                '年份': year,
                '建筑类型': house,
                '详情页': href,
            }
            csv_writer.writerow(dit)
            print(dit)
            # print(title, area, area_1, totalPrice, unitPrice, houseType, houseArea, houseFace, fitment, fool, year, house, href)
        # 请求网址/网站
        url = f'https://cs.lianjia.com/ershoufang/kaifu/pg{page}/'
        # 发送请求
        response = requests.get(url=url, headers=headers)
        # <Response [200]> 响应对象 200 状态码 表示请求成功
        print(response)
        """
        获取数据, 获取网页源代码 <获取服务器返回响应数据>

        解析数据, 提取我们想要的数据内容
            解析方法:
                1. re: 对于字符串数据直接进行解析提取
                2. css: 根据标签属性提取数据内容
                3. xpath: 根据标签节点提取数据内容

        css: 根据标签属性提取数据内容
        """
        # 把获取到html字符串数据, 转成可解析对象
        selector = parsel.Selector(response.text)
        # 获取所有房源信息所在li标签
        lis = selector.css('.sellListContent li.clear')
        # for循环遍历
        for li in lis:
            """
            提取具体房源信息: 标题 / 价格 / 位置 / 户型...
            .title a --> 表示定位class类名为title下面a标签
            """
            title = li.css('.title a::text').get()  # 标题
            info_list = li.css('.positionInfo a::text').getall()
            area = info_list[0]  # 小区名字
            area_1 = info_list[1]  # 地区
            totalPrice = li.css('.totalPrice span::text').get()  # 售价
            unitPrice = li.css('.unitPrice span::text').get().replace('元/平', '').replace(',', '')  # 单价
            houseInfo = li.css('.houseInfo::text').get().split(' | ')  # 信息
            houseType = houseInfo[0]  # 户型
            houseArea = houseInfo[1].replace('平米', '')  # 面积
            houseFace = houseInfo[2]  # 朝向
            fitment = houseInfo[3]  # 装修
            fool = houseInfo[4] if len(houseInfo) > 4 else '1'
            if len(houseInfo) == 7 and '年' in houseInfo[5]:
                year = houseInfo[5].replace('年建', '')
            else:
                year = ''
            house = houseInfo[-1]  # 建筑类型
            href = li.css('.title a::attr(href)').get()  # 详情页
            dit = {
                '标题': title,
                '小区': area,
                '区域': area_1,
                '售价': totalPrice,
                '单价': unitPrice,
                '户型': houseType,
                '面积': houseArea,
                '朝向': houseFace,
                '装修': fitment,
                '楼层': fool,
                '年份': year,
                '建筑类型': house,
                '详情页': href,
            }
            csv_writer.writerow(dit)
            print(dit)
            # print(title, area, area_1, totalPrice, unitPrice, houseType, houseArea, houseFace, fitment, fool, year, house, href)
        # 请求网址/网站
        url = f'https://cs.lianjia.com/ershoufang/furong/pg{page}/'
        # 发送请求
        response = requests.get(url=url, headers=headers)
        # <Response [200]> 响应对象 200 状态码 表示请求成功
        print(response)
        """
        获取数据, 获取网页源代码 <获取服务器返回响应数据>

        解析数据, 提取我们想要的数据内容
            解析方法:
                1. re: 对于字符串数据直接进行解析提取
                2. css: 根据标签属性提取数据内容
                3. xpath: 根据标签节点提取数据内容

        css: 根据标签属性提取数据内容
        """
        # 把获取到html字符串数据, 转成可解析对象
        selector = parsel.Selector(response.text)
        # 获取所有房源信息所在li标签
        lis = selector.css('.sellListContent li.clear')
        # for循环遍历
        for li in lis:
            """
            提取具体房源信息: 标题 / 价格 / 位置 / 户型...
            .title a --> 表示定位class类名为title下面a标签
            """
            title = li.css('.title a::text').get()  # 标题
            info_list = li.css('.positionInfo a::text').getall()
            area = info_list[0]  # 小区名字
            area_1 = info_list[1]  # 地区
            totalPrice = li.css('.totalPrice span::text').get()  # 售价
            unitPrice = li.css('.unitPrice span::text').get().replace('元/平', '').replace(',', '')  # 单价
            houseInfo = li.css('.houseInfo::text').get().split(' | ')  # 信息
            houseType = houseInfo[0]  # 户型
            houseArea = houseInfo[1].replace('平米', '')  # 面积
            houseFace = houseInfo[2]  # 朝向
            fitment = houseInfo[3]  # 装修
            fool = houseInfo[4] if len(houseInfo) > 4 else '1'

            if len(houseInfo) == 7 and '年' in houseInfo[5]:
                year = houseInfo[5].replace('年建', '')
            else:
                year = ''
            house = houseInfo[-1]  # 建筑类型
            href = li.css('.title a::attr(href)').get()  # 详情页
            dit = {
                '标题': title,
                '小区': area,
                '区域': area_1,
                '售价': totalPrice,
                '单价': unitPrice,
                '户型': houseType,
                '面积': houseArea,
                '朝向': houseFace,
                '装修': fitment,
                '楼层': fool,
                '年份': year,
                '建筑类型': house,
                '详情页': href,
            }
            csv_writer.writerow(dit)
            print(dit)
            # print(title, area, area_1, totalPrice, unitPrice, houseType, houseArea, houseFace, fitment, fool, year, house, href)
