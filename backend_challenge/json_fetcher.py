import urllib.request, json 

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