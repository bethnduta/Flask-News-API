import urllib.request,json
from .models import Articles,Sources

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    '''
    function that gets the json response to the url request
    '''

    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

    if get_news_response['articles']:
        news_results_list = get_news_response['articles']
        news_results = process_results(news_results_list) 
                        
    return news_results


def process_results(news_list):
        '''
        function that processes the movie result and transform them to a list of objects

        Args:
         news_list: a list of dictionaries that contain news details

         Returns:
         news results: a list of new objects
         '''
        news_results = []
        for news_item in news_list:
            title = news_item.get('title')
            description = news_item.get('description')
            urlToImage = news_item.get('urlToImage')
            content = news_item.get('content')
            publishedAt = news_item.get('publishedAt')
            news_object = Articles(title,description,urlToImage,content,publishedAt)
