from shopify_api import ShopifyAPI
from heap import Heap

class ShopifySolution():
    
    def __init__(self, api_url):
        api = ShopifyAPI(api_url)
        self.api = api
        self.orders = api.get_unfulfilled_orders()
        
        import random
        random.shuffle(self.orders)        

        self.available_cookies = api.get_stats().available_cookies
        self.priority_queue = Heap(self.compare_orders) 
        
    def print_result(self):
        for order in self.orders:
            self.priority_queue.insert(order)
            
        return self.orders
    

    
    def compare_orders(self, a, b):
        a_cookies = a.count_amount('Cookies')
        b_cookies = b.count_amount('Cookies')
        
        if a_cookies > b_cookies:
            return 1
        if (a_cookies == b_cookies and a.id < b.id):
            return 1
        return -1
    
api_url = 'https://backend-challenge-fall-2017.herokuapp.com/orders.json'
    
s = ShopifySolution(api_url)
s.print_result()
orders = s.orders
pq = s.priority_queue.data
print('..')