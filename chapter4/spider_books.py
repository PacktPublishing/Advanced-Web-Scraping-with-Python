import scrapy


class BooksSpider(scrapy.Spider):
    name = 'bookLinks'

    start_urls = ['http://books.toscrape.com']
    images_data = {}
	
    def parse(self, response):
        # follow links to author pages
        for img in response.css('a::attr(href)'):
            yield response.follow(img, self.parse_images)

    def parse_images(self, response):
        print ("URL: " + response.request.url)
        def extract_with_css(query):
            return response.css(query).extract()
        yield {
            'URL': response.request.url,
            'image_link': extract_with_css('img::attr(src)')
        }