from scrapy import Spider, Request
from gdoor.items import GdoorItem
import re

class GdoorSpider(Spider):

    name = 'gdoor_spider'
    allow_urls = ['https://www.glassdoor.com']
    start_urls = ['https://www.glassdoor.com/Job/data-science-jobs-SRCH_KO0,12.htm']

    def parse(self,response):

        result_list  = [f'https://www.glassdoor.com/Job/data-science-jobs-SRCH_KO0,12_IP{i}.htm' for i in range(2,31)]
        result_list.insert(0,'https://www.glassdoor.com/Job/data-science-jobs-SRCH_KO0,12.htm')

        print('length of urls=============' + '   ' + str(len(result_list)))

        for url in result_list:
            yield Request(url=url, callback=self.parse_result_url)

    def parse_result_url(self, response):

        lis = response.xpath('//ul[@class="jlGrid hover"]//li')
        with open('log.txt', 'a+') as f:
            f.write(str(len(lis))+ '\n')

        for li in lis:
            company = li.xpath('.//div[@class="jobInfoItem jobEmpolyerName"]/text()').extract_first()
            job_title = li.xpath('.//div[@class="jobContainer"]/a/text()').extract()[0]

            rating= li.xpath('.//span[@class="compactStars "]/text()').extract()
            duration = li.xpath('.//span[@class="minor"]/text()').extract()[0].strip()
            company_link = li.xpath('.//div[@class="jobHeader"]/a/@href').extract()[0].strip()
            company_link = 'https://www.glassdoor.com' + company_link

            try:
                location = li.xpath('.//div[@class="jobInfoItem empLoc"]/span/text()').extract_first()
            except Exceptionas as e:
                print('missing location')
                location = 'United States'

            try:
                start_salary = re.findall('\$\d+', ''.join(li.xpath('.//span/text()').extract()))[0].strip()
                max_salary = re.findall('\$\d+', ''.join(li.xpath('.//span/text()').extract()))[1].strip()
            except Exception as e:
                print('missing salary')
                start_salary = 'NA'
                max_salary = 'NA'

            item = GdoorItem()
            item['company'] = company
            item['job_title'] = job_title
            item['location'] = location
            item['rating'] = rating
            item['days_posted'] = duration
            item['start_salary'] = start_salary
            item['max_salary'] = max_salary
            item['job_link'] = company_link

            yield  item


