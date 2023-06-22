import psycopg2
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SrealityPipeline:
    def __init__(self):
        self.connection = None
        self.cur = None
    def open_spider(self, spider):
        hostname = 'db'
        username = 'sreality_user'
        password = 'sreality_pass'
        database = 'sreality'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO items (title, image_url) VALUES (%s, %s)", (item['title'], item['image_url']))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()


