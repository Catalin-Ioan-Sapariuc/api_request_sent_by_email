import requests, ssl
from send_email import send_email

api_key = "12ae71d82c284f77b7116adff4c5c82a"

url = "https://newsapi.org/v2/top-headlines?"\
       "country=us&category=business&apiKey="\
        "12ae71d82c284f77b7116adff4c5c82a" 

#password = input("Type your password and press enter:")
sender_email = "sapariuc@gmail.com" 

#from email.mime.text import MIMEText
                #from email.mime.multipart import MIMEMultipart

receiver_email = "catalinsapariuc8020@gmail.com"
                #receiver = sender
context = ssl.create_default_context()
# make a request
request = requests.get(url)

# get a dictionary from the request
content = request.json()

# extract articles
articles = content['articles']

body = '' 


for article in articles:
    #print(article['title'])
    try:
        body = body+ article['title'] + '  \n' + article['description'] +2 * ' \n' 
    except TypeError:
        pass

print(f'This is the content to be sent by email: \n {body}')

subject = 'This is an automated email which extracted information from newsapi.org, created using Python'
send_email(context, sender_email, receiver_email, subject , body)