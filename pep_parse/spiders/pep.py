import re
import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep_link in response.css(
                'section#numerical-index td a::attr(href)'):
            yield response.follow(pep_link, self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.xpath('//h1[@class="page-title"]/text()').get()
        number = int(
            re.search(r'^PEP\s(?P<number>\d+)\s–\s', pep_title).group('number')
        )
        yield PepParseItem({
            'number': number,
            'name': response.css('dt:contains("Author") + dd::text').get(),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get(),
        })
