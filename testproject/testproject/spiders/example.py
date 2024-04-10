
import scrapy


class NewSpider(scrapy.Spider):
    name = "Spy_crawler"

    def __init__(self, start_urls = None, max_pages = 5, *args, **kwargs: Any):
        super(NewSpider, self).__init__(*args, **kwargs)
        if start_urls:
            self.start_urls = start_urls.split(',')  # Split URLs by comma
        self.max_pages = int(max_pages)  # Convert max_pages to int
        self.pages_crawled = 0


    def parse(self, response):
        self.pages_crawled += 1 
        # check if the max  number of pages has been reached 
        if self.pages_crawled > self.max_pages: 
            self.crawler.engine.close_spider(self, 'Reached  max pages limit') 
        # 
        filename = f'page_{self.pages_crawled}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
    


