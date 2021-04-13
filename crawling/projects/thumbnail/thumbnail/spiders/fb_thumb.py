import scrapy
import csv

FB_THUMBNAIL_CSV_PATH = './facebook_thumbnail.csv'


class FbThumbSpider(scrapy.Spider):
    name = 'fb_thumb'
    def start_requests(self):
        with open(FB_THUMBNAIL_CSV_PATH) as in_file:
            csv_reader = csv.reader(in_file)
            base_url = "http://www.koodon.com/data/goods/"
            next(csv_reader)
            for row in csv_reader:
                product_code = row[2]
                image_storage = row[4]
                image_path = row[5]
                image_name = row[6]
                # print(product_code, image_storage, image_path, image_name)
                if not product_code:
                    # product_code 가 없는 row 는 패스.
                    continue
                if not image_name:
                    # 이미지 주소가 없으면 패스.
                    continue
                if image_storage == "url":
                    image_url = image_name
                elif image_storage == "local":
                    image_url = base_url + image_path + image_name
                yield scrapy.Request(image_url, callback=self.parse, cb_kwargs={'product_code': product_code})

    def parse(self, response, product_code):
        clean_image_urls = [response.url]

        yield {
            'image_urls': clean_image_urls,
            'product_code': product_code
        }


