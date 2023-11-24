import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse, parse_qs
import intro

seen_parameters = set()

def main(args):
    intro.intro(None, "\n ██▓███   ▄▄▄        ▄████ ▓█████      ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  \n▓██░  ██▒▒████▄     ██▒ ▀█▒▓█   ▀    ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒\n▓██░ ██▓▒▒██  ▀█▄  ▒██░▄▄▄░▒███      ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒\n▒██▄█▓▒ ▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄      ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  \n▒██▒ ░  ░ ▓█   ▓██▒░▒▓███▀▒░▒████▒   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒\n▒▓▒░ ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░\n░▒ ░       ▒   ▒▒ ░  ░   ░  ░ ░  ░   ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░\n░░         ░   ▒   ░ ░   ░    ░      ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ \n               ░  ░      ░    ░  ░         ░           ░  ░              ░  ░   ░     \n")
    global MySpider
    if args.spider_name:
        MySpider.name = args.spider_name

    if args.target:
        parsed_url = urlparse(args.target)
        if not parsed_url.scheme:
            args.target = "https://" + args.target

        MySpider.start_urls = [args.target]
        MySpider.allowed_domains = [urlparse(args.target).netloc]

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
            query_params = parse_qs(parsed_url.query)
            unique_params = {k: v[0] for k, v in query_params.items() if k not in seen_parameters}
            seen_parameters.update(unique_params.keys())

            if unique_params:
                updated_query = "&".join([f"{k}={v}" for k, v in unique_params.items()])
                cleaned_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{updated_query}"
                
                with open("sql_urls.txt", "a") as f:
                    f.write(cleaned_url + "\n")

        yield {
            'url': response.url,
        }
