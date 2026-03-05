import requests

class MetalsClient:
    BASE_URL = 'https://metals-api.com/api/'

    def __init__(self, access_key):
        self.access_key = access_key

    def get_prices(self, currencies=['USD'], metals=['XAU', 'XAG']):
        endpoint = f'{self.BASE_URL}latest'
        params = {
            'access_key': self.access_key,
            'currencies': ','.join(currencies),
            'metals': ','.join(metals)
        }
        response = requests.get(endpoint, params=params)
        return response.json()

    def get_price(self, metal, currency='USD'):
        prices = self.get_prices(currencies=[currency], metals=[metal])
        return prices.get('rates', {}).get(metal, None)

# Usage example:
# client = MetalsClient('YOUR_ACCESS_KEY')
# print(client.get_prices())
# print(client.get_price('XAU'))