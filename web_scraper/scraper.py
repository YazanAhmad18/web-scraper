import requests  
from bs4 import BeautifulSoup

request_URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


def  get_citations_needed_count(url):
    response=requests.get(url)
    soup=BeautifulSoup( response.text, 'html.parser' )
    result=soup.find_all( 'sup', class_ = 'Inline-Template' )
    return (len(result))


def get_citations_needed_report(url):

    response = requests.get(url)
    soup = BeautifulSoup( response.text, 'html.parser' )
    # result = soup.find_all( 'a', title='Wikipedia:Citation needed' )
    result=soup.find_all( 'sup', class_ = 'Inline-Template' )
    paragraph_contain_citation = []

    for p in result:
        paragraph_contain_citation.append(p.parent.text.strip())
    return '\n'.join(paragraph_contain_citation)



if __name__=='__main__':

    print(get_citations_needed_report(request_URL))
    print(get_citations_needed_count(request_URL))

