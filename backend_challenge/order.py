class Order():
    
    class Product():
        def __init__(self, p_summary):
            self.title = p_summary['title']
            self.amount = p_summary['amount']
            
    def __init__(self, summary):
        self.id = summary['id']
        self.fulfilled = True if summary['fulfilled'] == 'true' else False
        self.products = [ self.Product(product) for product in summary['products'] ]