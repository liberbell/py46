import scrapy


class QiitaTrend1dSpider(scrapy.Spider):
    name = 'qiita_trend_1d'
    allowed_domains = ['qiita.com']
    start_urls = ['http://qiita.com/']

    def parse(self, response):
        category = response.xpath("/html/body/div[1]/div[1]/nav/div/a[1]/text()").get()
        titles = response.xpath("//h2/a/text()").getall()
        urls = response.xpath("//h2/a/@href").getall()

        # category = response.css("nav > div > a.style-c221vd::text").get()
        # titles = response.css('h2 > a::text').getall()
        # urls = response.css('h2 > a::attr(href)').getall()

        yield {
            'category': category,
            'titles': titles,
            'urls': urls
        }
