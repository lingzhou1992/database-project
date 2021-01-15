import scrapy
from scrapyProject.items import ScrapyprojectItem

class ZillowSpider(scrapy.Spider):
    name = 'zillow'
    zipCode = [
        94002, 94005, 94010
    ]

    base_url_part1 = 'https://www.zillow.com/homes/'
    base_url_part2 = '_rb/'
    url_list = []
    for code in zipCode:
        url = base_url_part1 + str(code) + base_url_part2
        url_list.append(url)

    start_urls = url_list


    def parse(self, response):

        for house in response.xpath('.//div[@class="list-card-info"]/a/@href'):
            yield scrapy.Request(
                response.urljoin(house.extract()),
                callback=self.parse_page
            )

        next_page = response.xpath('.//a[@title="Next page"]/@href').extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    def parse_page(self, response):
        item = ScrapyprojectItem()

        item['price'] = response.xpath('.//div[@class="ds-summary-row"]//span/text()').extract_first()
        item['type'] = response.xpath('.//ul[@class="ds-home-fact-list"]/li[1]/span[2]/text()').extract_first()
        item['year'] = response.xpath('.//ul[@class="ds-home-fact-list"]/li[2]/span[2]/text()').extract_first()
        item['lot_size'] = response.xpath('.//ul[@class="ds-home-fact-list"]/li[last()-1]/span[2]/text()').extract_first()
        item['price_per_sqft'] = response.xpath('.//ul[@class="ds-home-fact-list"]/li[last()]/span[2]/text()').extract_first()
        item['street'] = response.xpath('.//div[@class="ds-home-details-chip"]/div[2]//header//span[1]/text()').extract_first()
        item['city_state'] = response.xpath('.//div[@class="ds-home-details-chip"]/div[2]//header//span[2]/text()[2]').extract_first()
        item['bedrooms'] = response.xpath('.//h3[@class="ds-bed-bath-living-area-container"]/span[1]/span/text()').extract_first()
        item['size'] = response.xpath('//h3[@class="ds-bed-bath-living-area-container"]/span[last()]/span[1]/text()').extract_first()
        item['bathrooms'] = response.xpath('.//h3[@class="ds-bed-bath-living-area-container"]//*[3]//span/text()').extract_first()
        item['time_on_zillow'] = response.xpath('.//div[@class="ds-overview"]//div[@class="sc-oVdHe bsLHzL"][1]/div[2]/text()').extract_first()
        item['views'] = response.xpath('.//div[@class="ds-overview"]//div[@class="sc-oVdHe bsLHzL"][2]/div[2]/text()').extract_first()
        item['saves'] = response.xpath('.//div[@class="ds-overview"]//div[@class="sc-oVdHe bsLHzL"][3]/div[2]/text()').extract_first()
        item['neighborhood'] = response.xpath('.//span[@id="skip-link-neighborhood"]/following-sibling::div/h4/text()').extract_first()


        yield item