from django.shortcuts import render
import requests

# Create your views here.
def home_view(request):
    # define news category
    category = [
        'technology',
        'sports',
        'health',
        'business',
        'entertainment',
        'general',
        'software',
        'bollywood',
        'politics',
    ]

    dict = {'category':category}
    return render(request,'newsapp/home.html', context=dict)
    
    

def news_view(request, category):
    API_KEY =  'fabc2cf73d0f49da85eb80bf224ef15d'
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=fabc2cf73d0f49da85eb80bf224ef15d"


    response = requests.get(url)
    data = response.json()

    # extract aricles lists from API
    articles = data.get('articles' ,[]) if data.get('status') == 'ok' else[]

    dict = {
        'articles':articles,
        'category':category,
    }

    return render(request, 'newsapp/news_list.html',context=dict)