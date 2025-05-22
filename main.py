import requests

api_key = "12ae71d82c284f77b7116adff4c5c82a"

url = "https://newsapi.org/v2/top-headlines?"\
       "country=us&category=business&apiKey="\
        "12ae71d82c284f77b7116adff4c5c82a" 

# make a request
request = requests.get(url)

# get a dictionary from the request
content = request.json()

# extract articles
articles = content['articles']

for article in articles:
    print(article['title'])
    print(article['description'])