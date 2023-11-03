import requests
from bs4 import BeautifulSoup
import re
import json

base_url = "https://gtfobins.github.io/#+sudo"
# If you want to skip tool/s add them in here
tools = []#['vim','bash','docker','make','nice','nmap','node','pexec','aa-exec','ansible-test','apt-get','apt','ash','bash','cpulimit','dash']
# Send an HTTP GET request to the base URL
response = requests.get(base_url)
files = 0
sus = 0
with open("su.json", "r") as f:
        dataS = json.load(f)
with open("file.json", "r") as f:
        dataF = json.load(f)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all links with the pattern /gtfobins/ followed by then tools name
    links = soup.find_all("a", href=re.compile(r'^/gtfobins/([^/]+)/$'))

    # Extract and print the random names
    for link in links:
        url = link["href"]
        toolName_match = re.match(r'^/gtfobins/([^/]+)/$', url)
        toolName = toolName_match.group(1)
        print(toolName)
        if toolName not in tools:
            url = f"https://gtfobins.github.io/gtfobins/{toolName}"
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                # Find the h2 element with id "sudo"
                sudo_h2 = soup.find("h2", {"id": "sudo"})

                if sudo_h2:
                    # Find the ul element after the h2 element
                    ul_element = sudo_h2.find_next("ul")

                    if ul_element:
                        # Find the li element inside the ul element
                        li_element = ul_element.find("li")

                        if li_element:
                            # Find the code element inside the li element
                            code_element = li_element.find("code")

                            if code_element:
                                code_text = code_element.get_text().replace("\n", "; ").replace('"', "'")
                                if "less" in code_text:
                                    print("weird command")
                                elif "file" in code_text:
                                    files = files+1
                                    dataF["cmds"][toolName] = code_text
                                else:
                                    sus = sus+1
                                    dataS["cmds"][toolName] = code_text
                            else:
                                print("No code element found inside the li element.")
                        else:
                            print("No li element found inside the ul element.")
                    else:
                        print("No ul element found after the h2 element with id 'sudo'.")
                else:
                    print("No h2 element found with id 'sudo'.")
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")
    print("total of {} root PrivEscs found".format(sus))
    print("total of {} file PrivEscs found".format(files))
    with open("su.json", "w") as f:
        json.dump(dataS, f, indent=4)
    with open("file.json", "w") as f:
        json.dump(dataF, f, indent=4)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
