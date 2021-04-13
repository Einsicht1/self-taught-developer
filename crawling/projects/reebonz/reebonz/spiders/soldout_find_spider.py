import csv
import scrapy
from scrapy_splash import SplashRequest


CSV_PATH = 'reebonz1.csv'

reebonz_urls = {}
with open(CSV_PATH) as in_file:
    csv_reader = csv.reader(in_file)
    next(csv_reader)
    for row in csv_reader:
        product_code = row[1]
        reebonz_url = row[2]
        reebonz_urls[reebonz_url] = product_code


class SoldoutFindSpider(scrapy.Spider):
    name = "soldout"
    script = '''
        function main(splash, args)
            splash:set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.37")
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return {
            html = splash:html(),
            }
        end
    '''

    def start_requests(self):
        urls = reebonz_urls
        for url in urls.keys():
            yield SplashRequest(url=url, callback=self.parse, endpoint="execute", args={'lua_source': self.script})

    def parse(self, response):
        res = response.body.decode('utf-8')
        if "1개 남음" in res:
            pass
        else:
            if 'redirect_urls' in response.request.meta.keys():
                origin_url = response.request.meta['redirect_urls'][0]
                yield {
                    "url" : origin_url,
                    "product_code": reebonz_urls[origin_url]
            }
            else:
                yield {
                    "url" : response.url,
                    "product_code": reebonz_urls[response.url]
                }
