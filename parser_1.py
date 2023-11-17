from newspaper import Article

# Функция для парсинга статьи
def parse_article(url):
    article = Article(url, language="ru")
    article.download()
    article.parse()
    return article

article_url = "https://www.iubip.ru/news/282/"

while True:
    article = parse_article(article_url)

    title = article.title
    text = article.text[:500]

    print("Заголовок:", title)
    print("Текст статьи:", text)

    answer = input("Хотите увидеть следующую новость? (да/нет): ")
    if answer.lower() != 'да':
        break

    # Генерация ссылки на следующую статью
    article_number = int(article_url.split("/")[-2])  # Получаем номер статьи из URL
    next_article_number = article_number + 1
    next_article_url = f"https://www.iubip.ru/news/{next_article_number}/"
    article_url = next_article_url