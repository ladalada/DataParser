import bs4 as bs
import urllib.request
import re

def get_soup(link):
    source = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    return soup

def html_links(source_link):
    try:
        source_soup = get_soup(source_link)
    except ValueError:
        return 'no such site'
    
    links = []
    for a in source_soup.find_all('a'):
        href = a.get('href')
        if href !=  None and href != '#' and href != '/':
            links.append(a.get('href'))
    result = ',\n'.join(links)
    return result

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def html_text(source_link):
    result = ''
    try:
        soup = get_soup(source_link)
    except ValueError:
        return 'no such site'

    result += soup.html.head.title.string
    result += '\n\n'

    contents = soup.contents[1].contents[3].contents
    for content in contents:
        if content.name == 'script' or content.name == None:
            continue
        result += content.text

    result = re.sub(r'^\s+|\n|\s+$', '', result)
    return result
