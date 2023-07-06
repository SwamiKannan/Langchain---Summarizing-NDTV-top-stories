import sys
from News import News_Scraper
import requests
import pickle
from bs4 import BeautifulSoup


# url = 'https://www.ndtv.com/latest'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/50.0.2661.102 Safari/537.36'}

# dict={'sports':'<div class="story__content',
#       'gadgets360':"'div', class_='content_text row description'"}

class NDTV_scraper(News_Scraper):
    def __init__(self):
        super().__init__()
        # self.headers=headers
        self.summaries = []
        self.url = 'https://www.ndtv.com/latest'

    def extract_heads(self):
        self.response = requests.get(url=self.url, headers=self.headers)
        self.page = self.response.text
        self.soup = BeautifulSoup(self.page, 'html.parser')
        news = self.soup.find_all(name="div", class_="news_Itm")
        for div in news:
            try:
                summary = div.find_all(name='p', class_='newsCont')[0].text
                self.summaries.append(summary)
                self.headlines.append(div.find_all(name='h2')[0].text)
                self.urls.append(div.find('a')['href'])
            except:
                pass

    def parse_food_ndtv(self, url):
        final_content_list = []
        response = requests.get(url, self.headers).text
        soup = BeautifulSoup(response, 'html.parser')
        remove_strong = soup.find_all('strong')
        remove_ahref = soup.find_all('a')
        for a in remove_ahref:
            a.decompose()

        inter1 = soup.find_all(name='div', class_="sp_only-ul-ol")[0]
        inter2 = inter1.find_all(name='p')
        for inter in inter2:
            inter.text.replace('Read Also', ' ') if 'Read Also' in inter.text else inter.text
            inter.text.replace('Advertisement', ' ') if 'Advertisement' in inter.text else inter.text
            print('****FOOD CONTENT****')
            print(inter.text)
            final_content_list.append(inter.text)
            final_content=' '.join(final_content_list)
        return final_content

    def get_main_content(self, url):
        response = requests.get(url, self.headers)
        if response.status_code != 200:
            print(response.status_code)
            return None
        # print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)
        try:
            content1 = soup.find_all('div', {"itemprop": "articleBody"})  # Mostly, all sections
            content = content1[0].text
            print('Content:', content)
            print('First shot')
        except:
            try:
                content1 = soup.find_all('div', class_="content_text row description")  # Gadgets.ndtv
                content = content1[0].text
                # print('Content:', content)
                # print('Second shot')
            except:
                try:
                    content1 = soup.find_all('div', class_="story__content")  # Sports.ndtv
                    content = content1[0].text
                    # print('Content:', content)
                    # print('Third shot')
                except:
                    try:
                        content1 = soup.find_all('div', {"itemprop": "articleBody"})  # Doctor.ndtv
                        content2 = content1.find_all(name='p')
                        content = content2[0].text
                        # print('Content:', content)
                        # print('Fourth shot')
                    except Exception as e:
                        # print('No content for url',url)
                        print(e)
                        return "No content"

        return content

    def extract_text(self):
        self.articles = []
        for link in self.urls:
            if 'sports.ndtv.com' in link:  # food and sports need to be parsed separately
                print('Sports inside')
                self.articles.append('No content for sports')
            elif 'food.ndtv.com' in link :
                article=self.parse_food_ndtv(link)
                self.articles.append(article)
            else:
                article = self.get_main_content(link)
                self.articles.append(article)

    def run_extraction(self):
        self.extract_heads()
        self.extract_text()
        return self.headlines, self.summaries, self.articles, self.urls


ndtv_test = NDTV_scraper()
ndtv_content = ndtv_test.run_extraction()
hl, summ, art, urls = ndtv_content

print('**********************FINAL***********************')
print(len(hl))
print(len(summ))
print(len(art))
print(len(urls))

print('*************************DETAILS*******************')

for h,s,a,u in zip(hl, summ, art, urls):
    print('url')
    print(u)
    print('headline')
    print(h)
    print('article')
    print(a)
    print('summary')
    print(s)

print('*****************************FINAL_DICT*******************************')

dict_news = {i: content for i, content in enumerate(zip(hl, summ, art, urls))}
print(len(dict_news))

sys.setrecursionlimit(5000)

with open('data.pkl','wb') as f:
    pickle.dump(dict_news,f,protocol=pickle.HIGHEST_PROTOCOL)
