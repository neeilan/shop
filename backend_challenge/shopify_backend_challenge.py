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
        '''
        Prints the JSON-format report containing the number of remaining cookies
        and the list of ascending unfulfilled order id's
        '''
        
        unfulfilled = []
        
        for order in self.orders:
            self.priority_queue.insert(order)
            
        while not self.priority_queue.is_empty():
            curr_order = self.priority_queue.remove_top()
            num_cookies = curr_order.count_amount(self.cookie_key)
            
            if num_cookies > self.available_cookies:
                unfulfilled.append(curr_order.id)
            else:
                self.available_cookies -= num_cookies
            

        unfulfilled.sort()
        print ({ "remaining_cookies" : self.available_cookies, "unfulfilled_orders" : unfulfilled })
    

    def compare_orders(self, a, b):
        '''
        Comparator function for comparing priorities of two orders. Ordering is
        done by cookie count, or by id if the cookie counts are the same.
        '''
        a_cookies = a.count_amount(self.cookie_key)
        b_cookies = b.count_amount(self.cookie_key)
        
        if a_cookies > b_cookies:
            return 1
        if (a_cookies == b_cookies and a.id < b.id):
            return 1
        return -1
 
if __name__ == '__main__':  
    api_url = 'https://backend-challenge-fall-2017.herokuapp.com/orders.json'
    s = ShopifySolution(api_url)
    s.print_result()
