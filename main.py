from src.ndtv_class import NDTV_scraper
from src.summarizer import summarize_news
from src.create_newspaper import open_newspaper


def main():
    ndtv_scraper = NDTV_scraper()
    ndtv_content = ndtv_scraper.run_extraction()
    hl, summ, art, urls = ndtv_content
    dict_news = {i: content for i, content in enumerate(zip(hl, summ, art, urls))}
    print(len(dict_news))

    sys.setrecursionlimit(5000)

    with open('data.pkl', 'wb') as f:
        pickle.dump(dict_news, f, protocol=pickle.HIGHEST_PROTOCOL)
    summarize_news()
    open_newspaper('summary.pkl', 'ndtv_summary.html')
    return None

if __name__=="__main__":
    main()