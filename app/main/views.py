from flask import render_template
from . import main
from .. request import get_news

@main.route('/')
def index():
    '''
    view route page function that returns the index page and its data
    '''
    news = get_news()
    title = 'NEWSAPI'
    return render_template('index.html', title=title, articles=news)