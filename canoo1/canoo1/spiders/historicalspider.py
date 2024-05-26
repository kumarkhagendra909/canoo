import scrapy
from canoo1.items import HistoricalSpiderItem

class HistoricalspiderSpider(scrapy.Spider):
    name = "historicalspider"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/quote/GOEV/history"]

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }

    def __init__(self):
        print("History data collecting.......")

    def parse(self, response):
        print(f"Parsing historical... {response}")

        # Extracting data from the table
        rows = response.xpath('//table[@class="table svelte-ewueuo"]/tbody/tr')
        
        for row in rows:
            item = HistoricalSpiderItem()

            columns = row.xpath('td')
            
            # Check if the row has the expected number of columns
            if len(columns) != 7:
                print("Skipping a row due to unexpected structure.")
                continue
            
            # Extracting data from each column
            item["date"] = columns[0].xpath('text()').get().strip()
            item["open_price"] = columns[1].xpath('text()').get().strip()
            item["high_price"] = columns[2].xpath('text()').get().strip()
            item["low_price"] = columns[3].xpath('text()').get().strip()
            item["close_price"] = columns[4].xpath('text()').get().strip()
            item["adj_close"] = columns[5].xpath('text()').get().strip()
            item["volume"] = columns[6].xpath('text()').get().strip()
            
            print("========================================================================")
            print(item["date"], item["open_price"], item["high_price"], item["low_price"], item["close_price"], item["adj_close"], item["volume"])
            print("========================================================================")
            
            # Yield the extracted data
            yield item

# import scrapy


# class HistoricalspiderSpider(scrapy.Spider):
#     name = "historicalspider"
#     allowed_domains = ["finance.yahoo.com"]
#     start_urls = ["https://finance.yahoo.com/quote/GOEV/history"]

#     custom_settings = {
#         "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
#     }

#     def __init__(self):
#         print("History data collecting.......")

#     def parse(self, response):
#         print(f"Parsing historical... {response}")

#         # Extracting data from the table
#         rows = response.xpath('//table[contains(@class, "table")]/tbody/tr')

#         for row in rows:
#             # Extracting data from each row
#             date = row.xpath('td[1]/text()').get().strip()
#             open_price = row.xpath('td[2]/text()').get().strip()
#             high_price = row.xpath('td[3]/text()').get().strip()
#             low_price = row.xpath('td[4]/text()').get().strip()
#             close_price = row.xpath('td[5]/text()').get().strip()
#             adj_close = row.xpath('td[6]/text()').get().strip()
#             volume = row.xpath('td[7]/text()').get().strip()

#             print("========================================================================")
#             print(date, open_price, high_price, low_price, close_price, adj_close, volume)
#             print("========================================================================")

#             # Yield the extracted data
#             yield {
#                 "date": date,
#                 "open_price": open_price,
#                 "high_price": high_price,
#                 "low_price": low_price,
#                 "close_price": close_price,
#                 "adj_close": adj_close,
#                 "volume": volume,
#             }

#         # If there's a "Next" button or link, you can follow it to scrape more pages
#         # next_page = response.xpath('//a[@rel="next"]/@href').get()
#         # if next_page:
#             # yield response.follow(next_page, self.parse)


# # import scrapy


# # class HistoricalspiderSpider(scrapy.Spider):
# #     name = "historicalspider"
# #     allowed_domains = ["finance.yahoo.com"]
# #     start_urls = ["https://finance.yahoo.com/quote/GOEV/history"]

# #     custom_settings = {
# #     "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
# #     }
# # #     custom_settings = {
# # #     "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# # #    }


# #     def __init__(self):
# #         print("History data collecting.......")

# #     def parse(self, response):
# #         print(f"Parsing historical... {response}")
        
# #         # Extracting data from the table
# #         rows = response.css('.table.svelte-ewueuo')
# #         for row in rows:
# #             # Extracting data from each row
# #             date = row.css('td:nth-child(1)::text').strip()
# #             open_price = row.css('td:nth-child(2)::text').strip()
# #             high_price = row.css('td:nth-child(3)::text').strip()
# #             low_price = row.css('td:nth-child(4)::text').strip()
# #             close_price = row.css('td:nth-child(5)::text').strip()
# #             adj_close = row.css('td:nth-child(6)::text').strip()
# #             volume = row.css('td:nth-child(7)::text').strip()
# #             print("========================================================================")
# #             print(date, open_price, high_price, low_price, close_price, adj_close, volume)
# #             print("========================================================================")

# #             # You can process or store the extracted data here
# #             yield {
# #                 "data": date,
# #                 "open_price": open_price,
# #                 "high_price": high_price,
# #                 "low_price": low_price,
# #                 "close_price": close_price,
# #                 "adj_close": adj_close,
# #                 "volume": volume,
# #             }
# #         # If there's a "Next" button or link, you can follow it to scrape more pages
# #         # next_page = response.css('a.next_page::attr(href)').get()
# #         # if next_page is not None:
# #         #     yield response.follow(next_page, self.parse)