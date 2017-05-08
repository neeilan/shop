from shopify_api import ShopifyAPI
from heap import Heap

class ShopifySolution():
    
    def __init__(self, api_url):
        api = ShopifyAPI(api_url)
        self.api = api
        self.orders = api.get_unfulfilled_orders()
        self.available_cookies = api.get_stats().available_cookies
        self.priority_queue = Heap(self.compare_orders) 
        self.cookie_key = 'Cookie'
        
    def print_result(self):
        for order in self.orders:
            self.priority_queue.insert(order)
            
        unfulfilled = []
        
        while not self.priority_queue.is_empty():
            curr_order = self.priority_queue.remove_top()
            num_cookies = curr_order.count_amount(self.cookie_key)
            print(num_cookies)
            if num_cookies > self.available_cookies:
                unfulfilled.append(curr_order.id)
            else:
                self.available_cookies -= num_cookies
            
        unfulfilled.sort()
        print ({ "remaining_cookies" : self.available_cookies, "unfulfilled_orders" : unfulfilled})
    

    
    def compare_orders(self, a, b):
        a_cookies = a.count_amount(self.cookie_key)
        b_cookies = b.count_amount(self.cookie_key)
        
        if a_cookies > b_cookies:
            return 1
        if (a_cookies == b_cookies and a.id < b.id):
            return 1
        return -1
    
api_url = 'https://backend-challenge-fall-2017.herokuapp.com/orders.json'
s = ShopifySolution(api_url)
s.print_result()
