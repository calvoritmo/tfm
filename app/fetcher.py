import graph
import fetch

articles = fetch.FetchModel.random_articles(1000)

for title in articles:
  print(f'Fetching {title}:', end=' ')
  article = fetch.FetchModel.fetchWP(title)
  f = fetch.WikipediaHTML.generate(article, None)
  print(f'{f.uuid}')
  f.asGraph().save(f'../import/fetch/{f.uuid}.ttl')
  with open(f'../import/fetch/{f.uuid}.html', 'w', encoding='utf-8') as file:
    file.write(article)