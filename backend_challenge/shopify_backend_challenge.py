import urllib.request, json 
import math

class JSONFetcher():
    def __init__(self, base_url):
        self.base_url = base_url
    
    def fetch(self, query = {}):
        query_url = self._build_query_url(query)
        with urllib.request.urlopen(query_url) as url:
            data = json.loads(url.read().decode())
            return data

    def _build_query_url(self, query):
        if query == {}:
            query_url = self.base_url
        else:
            query_str = '/?'
            for param in query:
                query_str += '{0}={1}'.format(param, query[param])
                query_url = self.base_url + query_str
        return query_url
        
        
class ShopifyAPI():
    
    def __init__(self, api_url):
        self.api_url = api_url
        self.fetch = JSONFetcher(api_url).fetch
        
    def get_stats(self):
        return self.fetch()['pagination']
    
    def get_orders_on_page(self, page_num = 1):
        return self.fetch({ 'page' : page_num })['orders']
    
    def get_all_orders(self):
        orders = []
        stats = self.get_stats()
        num_pages = math.ceil(stats['total'] / stats['per_page'])
        
        for pg_num in range(1, num_pages + 1):
            orders += self.get_orders_on_page(pg_num)
            
        return orders

class ShopifySolution():
    
    def __init__(self, api_url):
        self.orders = [order for order in ShopifyAPI(api_url).get_all_orders()]
        
    def print_result(self):
        pass
    
api_url = 'https://backend-challenge-fall-2017.herokuapp.com/orders.json'
    
s = ShopifySolution(api_url)
