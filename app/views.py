from flask import render_template
from app import app
from .request import get_news, get_news, search_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular news, upcoming current,regional and television news
    popular_news = get_news('popular')
    # business_news = get_news('business')
    # techCrunch_news = get_news('techCrunch')
    # publishedAt_news= get_news('publishedAt')
    title = 'Home - Welcome to The best News Articles Website Online'
    return render_template('index.html', title = title,popular = popular_news)
    


@app.route('/news/<category>')
def news(category):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(category)
    # print(news.author)
    title = f'You are reading {news.title}'
    return render_template('news.html',title = title,news=news)

@app.route('/search/<news_title>')
def search(news_title):
    '''
    View function to display the search results
    '''
    news_title_list = news_title.split(" ")
    news_title_format = "+".join(news_title_list)
    searched_news = search_news(news_title_format)
    title = f'search results for {news_title}'
    return render_template('search.html',news = searched_news)