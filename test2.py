from urllib.parse import urlparse, urlunparse

input_url = "scheme://subdomain1.subdomain2.url/path/to/resource?param1=value1&param2=value2"  # Replace with your input URL

parsed_url = urlparse(input_url)

# Keep the scheme and top-level domain, remove subdomains, path, and query parameters
modified_url = urlunparse(parsed_url._replace(netloc='.'.join(parsed_url.netloc.split('.')[-2:]), path='', query=''))

print("Original URL:", input_url)
print("Modified URL:", modified_url)
