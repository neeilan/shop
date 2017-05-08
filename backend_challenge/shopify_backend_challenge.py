import urllib.request, json 


    


  
    

        
api_url = 'https://backend-challenge-fall-2017.herokuapp.com/orders.json'

print ( get_orders_on_page(api_url, 3) )


class JSONFetcher():
    def __init__():
        pass
    
    def fetch(query_url):
        with urllib.request.urlopen(query_url) as url:
            data = json.loads(url.read().decode())
            return data
        
class ShopifyAPI():
    
    def __init__(self, api_url):
        self.api_url = api_url
        self.fetch = JSONFetcher().fetch
        
    def get_orders_on_page(self, page_num = 1):
        query_url = '{0}?page={1}'.format(self.api_url, page_num)
        return self.fetch(query_url)['orders']
    
    def get_summary(self):
        return self.fetch(self.api_url)['pagination']
    
    def get_all_orders(self):
        order_summary = self.get_summary()

class ShopifySolution():
    
    def __init__(self, api_url):
        pass
    
    def print_result(self):
        pass
    
