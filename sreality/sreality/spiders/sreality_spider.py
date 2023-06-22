import scrapy
from sreality.items import SrealityItem


class SrealitySpiderSpider(scrapy.Spider):
    name = "sreality_spider"
    allowed_domains = ["www.sreality.cz"]
    start_urls = ["https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=10"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        response = response.json()
        for item in response["_embedded"]["estates"]:
            title = item["name"]
            image_urls_set = {image['href'] for image in item['_links']['images']}
            image_url = list(image_urls_set)
            flat = SrealityItem(title=title, image_url=image_url)
            yield flat
