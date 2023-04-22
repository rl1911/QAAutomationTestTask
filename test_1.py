import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import re
import pytest

@dataclass
class website:   
    website_name: str
    visitors: int
    front_end: str
    back_end: str
    database: str
    notes: str

def parseNumberOfVisitor(numberOfVisitor):
    numberOfVisitor = re.match("^([\d\.,]*)", numberOfVisitor).group(1)
    numberOfVisitor = re.sub("[\.,]", "", numberOfVisitor)
    return int(numberOfVisitor)

def removeSquareBrackets(text):
    text = re.sub("\[[\d]*\]", "", text)
    text = re.sub("\\n", "", text)
    #text = re.sub("\n", "", text)
    return text

websites = []

operations = [(10**7), (1.5 * 10**7), (5 * 
10**7), (10**8), (5 * 10**8), (10**9), (1.5 * 10**9)
]

@pytest.mark.parametrize('number_operation', operations)
def test_pytest(number_operation):    
    response = requests.get("https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites")
    page_html = response.text
    page = BeautifulSoup(page_html, 'html.parser')
    table_body = page.findAll("tbody")[0] #получаем первую таблицу
    tr_array = table_body.findAll("tr")[1:] #получаем строки таблицы и отбрасываем строку хидера
    error_messages = []

    for row in tr_array:
        td_array = row.find_all('td')
        tr_website = website(removeSquareBrackets(td_array[0].text), parseNumberOfVisitor(td_array[1].text), \
                    removeSquareBrackets(td_array[2].text), removeSquareBrackets(td_array[3].text), \
                          removeSquareBrackets(td_array[4].text), removeSquareBrackets(td_array[5].text))
        if (tr_website.visitors < number_operation):
            error_messages.append(f"{tr_website.website_name} (Frontend:{tr_website.front_end}\Backend:{tr_website.back_end})" \
                                  + f"has {str(tr_website.visitors)} unique visitors per month. (Expected more than {str(number_operation)})")
        websites.append(tr_website)

    assert len(error_messages) == 0, '; '.join(error_messages)
    