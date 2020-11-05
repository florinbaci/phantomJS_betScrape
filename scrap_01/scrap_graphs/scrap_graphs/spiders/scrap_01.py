import scrapy

class ScrapSpider(scrapy.Spider):
    name = 'title_text'    #variable name to run the crawl
    start_urls = [
        'https://ls.betradar.com/'
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext': title}