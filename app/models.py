class Articles:
    '''
    news articles class to define news object
    '''
def __init__(self,title,description,urlToImage,content,publishedAt,url):
    self.title = title
    self.description = description
    self.urlToImage = urlToImage
    self.content = content
    self.publishedAt = publishedAt
    self.url = url


class Sources:
    '''
    news sources class that defines the origin of the news
    '''

    def __init__(self, id, name, category,description):
        self.id = id
        self.name = name
        self.category = category
        self.description = description