from bs4 import BeautifulSoup
# import lxml
import requests
import json

### webpage test scraping #
# with open('website.html') as f:
# contents = f.read()
# print(cont_string, contents)

# soup = BeautifulSoup(contents, 'html.parser', )
# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)
# print(soup.li)
# print(soup.p)

# all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#     print(tag)
#     print(tag.getText())
#     print(tag.get('href'))
# print(all_anchor_tags)

# heading = soup.find(name='h1', id='name')
# print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)
# print(section_heading.name)
# print(section_heading.get('class'))
# print(section_heading.getText())

# company_url = soup.select_one(selector='p a')
# name = soup.select_one(selector='#name')
# print(company_url, name)
# print(name.getText(), company_url.getText(), company_url.get('href'))
# headings = soup.select('.heading')
# print(headings)

### Hacker News the most upvoted news scraping #
# resp = requests.get('https://news.ycombinator.com/news')
# yc_webpage = resp.text
# soup = BeautifulSoup(yc_webpage, 'html.parser')
# articles = soup.find_all('a', class_='storylink')
# upvotes_raw = soup.select('.subtext')
# # article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all('span', class_='score')]
# article_texts = []
# article_links = []
# article_upvotes = []
# for i in range(len(articles)):
#     article_texts.append(articles[i].getText())
#     article_links.append(articles[i].get('href'))
#     upvote_text = upvotes_raw[i].getText()
#     if 'points' in upvote_text:
#         article_upvotes.append(int(upvote_text.split()[0]))
#     else:
#         article_upvotes.append(0)
# max_score = max(article_upvotes)
# index = article_upvotes.index(max_score)
# print(article_texts[index], article_links[index], max_score)

### Empireonline 100 movies scraping #
empireonline_page = requests.get('https://www.empireonline.com/movies/features/best-movies-2').text
soup2 = BeautifulSoup(empireonline_page, 'html.parser')
# movies = soup2.find_all('h3', class_='jsx-4245974604')
script = soup2.find('script', id='__NEXT_DATA__')
string = str(script)
data = json.loads(string[string.index('{'):string.index('</')])
target = data['props']['pageProps']['apolloState']
movies = []
for k, v in target.items():
    if 'ImageMeta' in k:
        movies.append(v['titleText'])
movies = movies[::-1]
# print(movies)

with open('100movies.txt', 'w') as f:
    for i in range(len(movies)):
        movie = movies[i]
        if ')' in movie:
            movie = movie[movie.index(')')+2:]
        f.write(f'{i + 1}) {movie}\n')
