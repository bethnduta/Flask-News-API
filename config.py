import os

class Config:

    '''
    configuration parent class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-02&sortBy=publishedAt&apiKey=df87776a71c749458045ed641e8687cb'
    NEWS_API_KEY = os.environ.get('df87776a71c749458045ed641e8687cb')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production': ProdConfig
}    