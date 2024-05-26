import scrapy
from canoo1.items import ProfileSpiderItem

class ProfilespiderSpider(scrapy.Spider):
    name = "profilespider"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/quote/GOEV/profile"]

    custom_settings = {
        
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    
    }

    def __init__(self):
        print("Constructor running........")

    def parse(self, response):
        
        # print("Parsing profilespider")
        
        rows = response.xpath('//table[@class="svelte-mj92za"]/tbody/tr')
        
        for row in rows:
            item = ProfileSpiderItem()
            item["name"] = row.xpath("td[1]/text()").get().strip()
            item["title"] = row.xpath("td[2]/text()").get().strip()
            item["pay"] = row.xpath("td[3]/text()").get().strip()
            item["exercised"] = row.xpath("td[4]/text()").get().strip()
            item["year_born"] = row.xpath("td[5]/text()").get().strip()
            yield item
            test0 = row.xpath("td[0]/text()").get().strip()
            print("test0", test0)
            # print("Profile item", item)


# import scrapy

# class ProfilespiderSpider(scrapy.Spider):

#     name = "profilespider"
#     allowed_domains = ["finance.yahoo.com"]
#     start_urls = ["https://finance.yahoo.com/quote/GOEV/profile"]

#     custom_settings = {
#         "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }

#     def __init__(self):
#         print("Constructor running........")

#     def parse(self, response):

#         print("Parsing profile")
#         print(response)

#         # Extracting data from table rows
#         rows = response.xpath('//table[@class="svelte-mj92za"]/tbody/tr')

#         for row in rows:
#             name = row.xpath("td[1]/text()").get().strip()
#             title = row.xpath("td[2]/text()").get().strip()
#             pay = row.xpath("td[3]/text()").get().strip()
#             exercised = row.xpath("td[4]/text()").get().strip()
#             year_born = row.xpath("td[5]/text()").get().strip()
#             print(f"name {name} title {title} pay {pay} exercised {exercised} year_born {year_born}")

#             yield {
#                 "Name": name,
#                 "Title": title,
#                 "Pay": pay,
#                 "Exercised": exercised,
#                 "Year Born": year_born,
#             }