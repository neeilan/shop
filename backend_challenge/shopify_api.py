from json_fetcher import JSONFetcher
from order import Order
import math

class ShopifyAPI():
    
    class StatReport():
        def __init__(self, api_response):
            self.available_cookies = int(api_response['available_cookies'])
            self.total = int(api_response['pagination']['total'])
            self.per_page = int(api_response['pagination']['per_page'])
    
    def __init__(self, api_url):
        self.api_url = api_url
        self.fetch = JSONFetcher(api_url).fetch
        
    def get_stats(self):
        api_response =  self.fetch()
        return self.StatReport(api_response)
    
    def get_orders_on_page(self, page_num = 1):
        return [ Order(order) for order in self.fetch({ 'page' : page_num })['orders'] ]
    
    def get_all_orders(self):
        orders = []
        stats = self.get_stats()
        num_pages = math.ceil(stats.total / stats.per_page)
        
        for pg_num in range(1, num_pages + 1):
            orders += self.get_orders_on_page(pg_num)
            
        return orders
    
    def get_unfulfilled_orders(self):
        return [order for order in self.get_all_orders() if not order.fulfilled]