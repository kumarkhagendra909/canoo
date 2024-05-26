import scrapy
from canoo1.items import MainSpiderItem

class MainspiderSpider(scrapy.Spider):
    name = "mainspider"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/quote/GOEV"]

    def __init__(self):
        print("Constructor of Summary class ...")

    def parse(self, response):
        # print("parsing mainspider")
        ul_element = response.css("ul.svelte-tx3nkj")
        li_elements = ul_element.css("li.svelte-tx3nkj")

        for li in li_elements:
            label = li.css("span.label::text").get()
            value_span = li.css("span.value")
            fin_streamer = value_span.css("fin-streamer")

            if fin_streamer:
                value = fin_streamer.css("::text").get().strip()
            else:
                value = value_span.css("::text").get().strip()

            item = MainSpiderItem()
            item['label'] = label
            item['value'] = value
            yield item
        # print("Item",item)


# from typing import Any
# import scrapy


# class MainspiderSpider(scrapy.Spider):
#     name = "mainspider"
#     allowed_domains = ["finance.yahoo.com"]
#     start_urls = ["https://finance.yahoo.com/quote/GOEV"]

#     def __init__(self):
#         print("constructor of summary class ")

#     def parse(self, response):
#         # Find the <ul> element containing the data
#         ul_element = response.css("ul.svelte-tx3nkj")
#         li_elements = ul_element.css("li.svelte-tx3nkj")

#         # labellist, valuelist = list(), list()
#         # Iterate over each <li> element
#         for li in li_elements:
#             # Extract label
#             label = li.css("span.label::text").get()
#             # labellist.append(label)
#             # Check if the <span class="value"> contains <fin-streamer> elements
#             value_span = li.css("span.value")
#             fin_streamer = value_span.css("fin-streamer")

#             if fin_streamer:
#                 # If <span class="value"> contains <fin-streamer>, extract text from it
#                 value = fin_streamer.css("::text").get()
#                 # valuelist.append(value)
#             else:
#                 # If <span class="value"> does not contain <fin-streamer>, extract text directly
#                 value = value_span.css("::text").get()
#                 # valuelist.append(value)

#             # Print or yield the extracted data
#             yield {
#                 label: value.strip(),
#             }

