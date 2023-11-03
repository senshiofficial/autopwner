import requests
from bs4 import BeautifulSoup
import json
import threading
from urllib.parse import urlparse, urlunparse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.98 Safari/534.13 ChromePlus/1.5.3.0alpha4"
}
visited_urls = set()
base_url = "http://localhost"
json_urls = {
    base_url:{

    }
}

def scrape_pages(url = base_url):
    global visited_urls, json_urls
    try:
        raw_req = requests.get(url, headers=headers)
        soup = BeautifulSoup(raw_req.text, 'html.parser')

        links = soup.find_all('a', href=True)

        for link in links:
            href = link['href']
            
            if not href.startswith("http"):
                href = base_url+href
            parsed_url = urlparse(href)
            modified_url = urlunparse(parsed_url._replace(netloc='.'.join(parsed_url.netloc.split('.')[-2:]), path='', query=''))

            if modified_url == base_url and href not in visited_urls:
                print(href)
                visited_urls.add(href)
                scrape_forms(raw_req,href)
                scrape_pages(href)
                if parsed_url.query:
                    json_urls[base_url][href] = None
                    print("GET {}".format(href))
                    with open("urls.json", "w") as f:
                        f.write(json.dumps(json_urls, indent=4))
    except TypeError as e:
        pass
        #print(f"{e}")

def scrape_forms(html, url):
    soup = BeautifulSoup(html.text, 'html.parser')
    forms = soup.find_all('form')
    
    for form in forms:
        form_action = form.get('action')
        if not form_action or form_action.startswith('#'):
            form_action = url
        input_fields = form.find_all('input')
        data = {}
        for input_field in input_fields:
            name = input_field.get('name')
            if name:
                data[name] = input_field.get('value', '')
        for key, value in data.items():
            json_urls[base_url][url] = None
            json_urls[base_url][url][key] = value
        with open("urls.json", "w") as f:
            f.write(json.dumps(json_urls))

def main(args):
    global base_url
    if args.target:
        base_url = args.target
    if args.scrape_thread:
        for i in range(args.scrape_thread):
            thread = threading.Thread(target=scrape_pages)
            thread.start()
    else:
        scrape_pages()