import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blog'

    def start_requests(self):
        for i in range(2, 8):
            yield scrapy.Request(url=f"https://yoristory.tistory.com/{i}",
                                 callback=self.parse)

    def parse(self, response):
        title = response.xpath("//div[@class='hgroup']/h1/text()").get
        yield {"title": title}