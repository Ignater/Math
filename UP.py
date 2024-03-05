import requests
from bs4 import BeautifulSoup

link = "https://coinmarketcap.com./"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', class_='sc-beb003d5-2 bkNrIb')


n = 10
name_name = [0] * n
name_symbol = [0] * n
price_check = [0] * n
price = [0] * n
marketcap = [0] * n

for i in range(n):
     #Name_field
     name_name[i] = block.find_all(class_='sc-4984dd93-0 kKpPOn')[i].text
     name_symbol[i] = block.find_all(class_='sc-4984dd93-0 iqdbQL coin-item-symbol')[i].text

     #Price_field
     price_check = block.find_all(class_='sc-cadad039-0 clgqXO')[i]
     price[i] = price_check.find(class_='cmc-link').text

     #MarketCap_field
     marketcap[i] = block.find_all(class_='sc-edc9a476-0 fXzXSk')[i].text

     print(name_name[i], name_symbol[i], price[i], marketcap[i])

print('\n')
print("Введите название криптовалюты:")
print("Введите 'q'  для выхода")
while True:
    sh = input()
    if (sh == "q"):
        break

    for i in range(n):
        if (sh == name_name[i]):
            print('\n')
            print("Название\t\tСимвол\t\tЦена\t\tРыночная Капитализация")

            print(name_name[i], end='\t\t')

            print(name_symbol[i], end='\t\t')

            print(price[i], end='\t\t')

            print(marketcap[i], end='\t\t')
            print('\n')
        elif (sh not in name_name):
            print("Не правильные входные данные, попробуйте ещё раз:")
            break