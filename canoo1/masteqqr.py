from canoo1.spiders.profilespider import ProfilespiderSpider
from canoo1.spiders.mainspider import MainspiderSpider
from canoo1.spiders.historicalspider import HistoricalspiderSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == "__main__":

    # Initialize the CrawlerProcess
    process = CrawlerProcess(settings=get_project_settings())

    # Add your spiders to the process
    # summary 
    process.crawl(MainspiderSpider)
    # profile
    process.crawl(ProfilespiderSpider)
    # history
    process.crawl(HistoricalspiderSpider)
    # Start the crawling process
    def callback():
        print("All spiders have finished crawling. Perform any cleanup or additional actions here.")

    # Start the crawling process and pass the callback function
    process.start()

    callback() # at the end of the process