from bs4 import BeautifulSoup

page = open(r"06_Crawling\test01.html", 'rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())

#lst = list(soup.children)
#print(lst[2])

resultSet = soup.find_all('p')

for item in resultSet:
    print(item)