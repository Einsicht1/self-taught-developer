# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Request


# class ThumbnailPipeline:
#     def process_item(self, item, spider):
#         return item



class MyImagesPipeline(ImagesPipeline):

    #Name download version
    def file_path(self, request, response=None, info=None):
        product_code = request.meta['product_code']
        return f"{product_code}_thumb_.{request.url.split('.')[-1]}"

    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['image_urls'][0], meta={'product_code': item['product_code']})

