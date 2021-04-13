import scrapy


class WantedSpider(scrapy.Spider):
    name = 'wanted'

    def start_requests(self):
        url = "https://www.wanted.co.kr/search?query=%EB%B0%B1%EC%97%94%EB%93%9C"
        my_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        yield scrapy.Request(url, callback=self.parse, headers={"User-Agent": my_user_agent})

    def parse(self, response):
        print(response.body.decode('utf-8'))
