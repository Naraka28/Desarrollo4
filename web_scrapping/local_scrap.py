from bs4 import BeautifulSoup
import requests

# with open('../flask_blog/templates/layout.html') as html_file:
#     soup = BeautifulSoup(html_file, 'html.parser')
#     match = soup.find('title')
#     print(match)

dic = {}
base_url = 'https://quotes.toscrape.com/'
def scrap_page(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.content,'html.parser')
    return soup

def main(soup):
    #If you want to acces an attribute within the tag of the html like href, you acces it like a dictionary
    #for example like this:
    quote_attribute = soup.find('div',class_ = 'quote')['itemtype']
    tag_list = []
    print(quote_attribute)
    for quote in soup.find_all('div',class_='quote'):
        quote_post = quote.span.text
        quote_author = quote.small.text

        for tag in quote.find_all('a',class_='tag'):
            tag_list.append(tag.text)

        if quote_author in dic:
            dic[quote_author]["quotes"].append(quote_post)
        else:
            dic[quote_author] = {"quotes":[quote_post],"tags": tag_list}
        tag_list=[]
    return dic

def get_urls(dom,url_list:list)->list:
    url = dom.find('li',class_='next')
    if url is not None:
        next = url.a['href']
        next = f"{base_url}{next}"
        url_list.append(next)
        soup = scrap_page(next)
        return get_urls(soup, url_list)
    return url_list
if __name__ == '__main__':
    lista_urls = []
    soup = scrap_page(base_url)
    url = get_urls(soup,lista_urls)
    print(url)