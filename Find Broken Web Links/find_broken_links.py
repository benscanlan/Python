import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
import warnings
warnings.filterwarnings("ignore")
import time
cookies = {'acack': 'DAWTKNV323952cf8084a204fb20ab2508441a07d02d3d5dc9b7220b9044f94be2c39e058374a61ecf463716ef33d16cf9daf6331e884813b289f59a5aebca66a1e78b8c2423f0277e766e594dc22e5f99fde35a84705f12a19bea66a89b0cde9be38828196a912f38609006d0f550115201d2bb7ebcdae7b1268568609931bd91b3688154669cb5f1c9f36130da55c039412eb8cbc7ffd6a2beee0ba20aea1f46c9b65f937558a421e42eae169136ddf3d6190ae2a4df116e162a7d26419f9ad98c7a00a622b9e5d8f57b433b2409fb1260377815de3ff87499d6f8343e554b442d89b5cbeb84aec410ae61cc2165e89dd03f0e74e5e8dad5ebf22824bf594b99225afedbdbaf5a0fbc2ae4fc4c119854553b6d193ea7ba4e5655a125a120ed59c336045a6875f14fb704f043575347cdb8d2552ddce757f309cab82d90f31b5560010e8118ea22236250b0eb12cb92bb26c21c7cf42e381d171a3efb635d4a42efd6dd66c9c585a47V3'}
#f = open('searched_links.txt')
#i = open('broken_links.txt')
#searched_links = f.readlines()
#broken_links = i.readlines()
searched_links = []
broken_links = []
def getLinksFromHTML(html):
    def getLink(el):
        return el["href"]
    return list(map(getLink, BeautifulSoup(html, features="html.parser").select("a[href]")))

def find_broken_links(domainToSearch, URL, parentURL):
    if (not (URL in searched_links)) and (not URL.startswith("mailto:")) and (not ("javascript:" in URL)) and (not URL.endswith(".png")) and (not URL.endswith(".jpg")) and (not URL.endswith(".jpeg")):
        try:
            requestObj = requests.get(URL,cookies=cookies, verify=False);
            searched_links.append(URL)
            
            if(requestObj.status_code == 404):
                broken_links.append("BROKEN: link " + URL + " from " + parentURL)
                print(broken_links[-1])
                
            else:
                print("CHECKED: link " + URL + " from " + parentURL)
                if urlparse(URL).netloc == domainToSearch:
                    for link in getLinksFromHTML(requestObj.text):
                        find_broken_links(domainToSearch, urljoin(URL, link), URL)
        except Exception as e:
            print("ERROR: " + URL + " from " + parentURL);
            searched_links.append(domainToSearch)

find_broken_links(urlparse(sys.argv[1]).netloc, sys.argv[1], "")

print("\n--- DONE! ---\n")
print("The following links were broken:")

for link in broken_links:
    print ("\t" + link)
