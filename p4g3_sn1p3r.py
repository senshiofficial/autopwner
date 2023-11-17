import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
import intro

def main(args):
    intro.intro(None,"\n ██▓███   ▄▄▄        ▄████ ▓█████      ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  \n▓██░  ██▒▒████▄     ██▒ ▀█▒▓█   ▀    ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒\n▓██░ ██▓▒▒██  ▀█▄  ▒██░▄▄▄░▒███      ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒\n▒██▄█▓▒ ▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄      ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  \n▒██▒ ░  ░ ▓█   ▓██▒░▒▓███▀▒░▒████▒   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒\n▒▓▒░ ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░\n░▒ ░       ▒   ▒▒ ░  ░   ░  ░ ░  ░   ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░\n░░         ░   ▒   ░ ░   ░    ░      ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ \n               ░  ░      ░    ░  ░         ░           ░  ░              ░  ░   ░     \n")
    global MySpider
    if args.spider_name:
        MySpider.name = args.spider_name

    if args.target:
        parsed_url = urlparse(args.target)
        if not parsed_url.scheme:
            args.target = "https://" + args.target

        MySpider.start_urls = [args.target]
        MySpider.allowed_domains = [urlparse(args.target).netloc]
    #if args.allowed_domains:
    #    urls = str(args.allowed_domains).split()
    #    MySpider.allowed_domains.extend(urls)
    # Currently Not working
    
    process = CrawlerProcess({
        'LOG_LEVEL': 'ERROR',
    })
    MySpider.rules = (Rule(LinkExtractor(allow_domains=MySpider.allowed_domains), callback='parse_page', follow=True),)
    process.crawl(MySpider)
    process.start()


class MySpider(CrawlSpider):
    name = 'qwerty'
    allowed_domains = ''
    start_urls = ''
    custom_settings = {
        'USER_AGENT': 'Mozilla (7.1.10)',
    }

    def parse_page(self, response):
        print(f'\033[35m{response.url}\033[0m')
        parsed_url = urlparse(response.url)
        if parsed_url.query:
            with open("sql_urls.txt", "a") as f:
                f.write(response.url+"\n")
        yield {
            'url': response.url,
        }