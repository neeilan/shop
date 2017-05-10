import urllib.request, json 

class JSONFetcher():
    '''
    Simple class to fetch and parse JSON from the url specified by base_url (in
    constructor), with optional queries.
    
    '''
    def __init__(self, base_url):
        self.base_url = base_url
    
    def fetch(self, query = {}):
        '''
        Returns dictionary consisting of json-encoded data at base_url.
        query is a dictionary of query params and values that will be included
        in the GET request. Keys and values must be url-encoded prior to being
        added into the dictionary and passed in (if necessary)
        '''
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