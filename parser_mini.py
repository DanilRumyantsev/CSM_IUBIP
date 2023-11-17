from newspaper import Article

# Function to parse the article
def parse_article(url):
    article = Article(url, language="ru")
    article.download()
    article.parse()
    return article

article_url = "https://www.iubip.ru/news/282/"
article = parse_article(article_url)

title = article.title
text = article.text[:500]

print("Заголовок:", title)
print("Текст статьи:", text)