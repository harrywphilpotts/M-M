import requests

class NewsClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://newsapi.org/v2/'

    def get_mining_news(self):
        url = f'{self.base_url}everything?query=mining&apiKey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['articles']
        else:
            print(f'Error: {response.status_code}')
            return None

# Usage Example:
# client = NewsClient('your_api_key_here')
# mining_news = client.get_mining_news()
# print(mining_news)