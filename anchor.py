import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup, NavigableString, Tag
from urllib.request import Request, urlopen
#req = Request('https://www.thepythoncode.com', headers={'User-Agent': 'Mozilla/5.0'})
#html = urlopen(req)
#soup = BeautifulSoup(html.read(), 'lxml')
#links = []
#for link in soup.find_all('a'):
#    links.append(link.get('href'))
#print(links)


#names_tag = soup.find_all('a', {'class': 'dark showtimes-movie-title'})
#names = [name_tag.text for name_tag in names_tag]
#print(names)
def get_anchor(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    anchor_tag = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for body_child in soup.body.children:
        if isinstance(body_child, NavigableString):
            continue
        if isinstance(body_child, Tag):
            anchor_tag.append(body_child.name)
  #  urls = set()
  #  soup = BeautifulSoup(requests.get(url).content, "html.parser")

   # for a_tag in soup.find_all("a"):
    #    names = [anc.text for anc in a_tag]

    return anchor_tag

if __name__ == "__main__":
    tag = get_anchor("https://www.thepythoncode.com")
    file = open(r"C:\Users\Dell\Desktop\Output.txt", 'w')
    file.write(str(tag))
    file.close()
