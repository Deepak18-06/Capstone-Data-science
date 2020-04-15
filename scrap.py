from bs4 import BeautifulSoup
import request

with open('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup)