# import 3 modules ..
import requests
from bs4 import BeautifulSoup
import html5lib
# Enter URL
url = 'https://www.codewithharry.com/'
# Get Html
y = requests.get(url)
HtmlContent = y.content
# Parse Data from html
soup = BeautifulSoup(HtmlContent, 'html.parser')
# Tree Traversal / Making tree of Html
    # Prettify your html
    # soup.prettify()

title = soup.title
# print(type(soup))
Achchors = soup.find_all('a')
Paragraphs = soup.find_all('p')
# print(Achchors)
Classs = soup.find('p')['class']
find_all_classes = soup.find_all('p', class_="lead")
# print(find_all_classes)
getTXT = soup.find('p').get_text()
# print(getTXT)
# All link in page
simple = soup.find_all('a')
# print(simple)
empty = set()
for link in simple:
    if (link.get('href') != '#'):
        all = url+ link.get('href')
        empty.add(all)
# for item in empty:
#     print(item, end='\n')
comment = f'<a href="{"google.com"}">{"google"}</a>'
soup2 = BeautifulSoup(comment, 'html.parser')
# for new in soup.stripped_strings:
#     print(new)
search_toggle = soup.find(id='search-toggle')
# print(search_toggle.contents)
for cont in search_toggle.parent.parents:
    print(cont.name)
