from abc import abstractmethod, ABC

class News_Scraper(ABC):
    def __init__(self):
        self.url=None
        self.headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.headlines=[]
        self.urls=[]
        self.articles=[]
        self.soup=None

    @abstractmethod
    def extract_heads(self):
        pass

    def extract_text(self):
        pass

    def run_extraction(self):
        pass