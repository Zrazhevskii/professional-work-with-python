import bs4
import requests

URL = "https://habr.com/ru/all/"
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'PostgreSQL', 'IT', 'NetWare', 'Databricks', 'Simultaneity', 'NullReferenceException']
words = ['срезы по IT-рынку', 'активности найма в сентябре']

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

response = requests.get(URL, headers=headers)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")

for article in articles:
    date = article.find('time').text
    titles = article.find(class_='tm-article-snippet__title-link').find('span')
    title = titles.text
    # print(title)
    for i in KEYWORDS:
        if i in title:
            href = article.find('a', class_='tm-article-snippet__title-link').attrs['href']
            url = f'https://habr.com{href}'
            print(f'Дата: {date} - Заголовок: {title} - Ссылка: {url}')

