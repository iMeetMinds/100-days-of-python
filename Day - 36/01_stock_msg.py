import requests
import smtplib
import Dummy

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MSG_START = ""

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_info():
    parameters = {
        'function' : 'TIME_SERIES_DAILY',
        'symbol' : STOCK,
        'apikey' : Dummy.ALP_ADV_API_KEY
    }
    response = requests.get(url='https://www.alphavantage.co/query', params=parameters)
    response.raise_for_status()
    stock_data = response.json()

    return [float(n['4. close']) for n in [value for (key,value) in stock_data['Time Series (Daily)'].items()][1:3]]

def find_perc(num1, num2):
    global MSG_START
    perc = round(((100 * max(num1, num2)) / min(num1, num2)) - 100, 2)
    if num2 == max(num1, num2):
        MSG_START = f'{STOCK}: Up by {perc}%'
    if num1 == max(num1, num2):
        MSG_START = f'{STOCK}: Down by {perc}%'
    return perc

def get_news():
    parameters = {
        'q' : COMPANY_NAME,
        'language' : 'en',
        'pageSize' : 3,
        'apiKey' : Dummy.NEWS_API_KEY
    }

    response = requests.get(url='https://newsapi.org/v2/everything', params=parameters)
    response.raise_for_status()
    news_data = response.json()
    return news_data['articles']

def send_mail():
    with open("News.txt", "r") as file_data :
        msg = file_data.read()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=Dummy.MY_EMAIL, password=Dummy.MY_PASS)
        connection.sendmail(
            from_addr=Dummy.MY_EMAIL,
            to_addrs=Dummy.TO_EMAIL,
            msg=f"Subject : {MSG_START} \n\n {msg}"
        )

def create_news_file(news_message_str):
    with open("News.txt", "w") as file:
        file.write(news_message_str)
    send_mail()

def remove_non_ascii(s):
    return "".join(c for c in s if ord(c)<128)

stock_price = get_stock_info()
if find_perc(stock_price[0], stock_price[1]) >= 5:
    news_list = get_news()
    message_str = ""
    for news_dict in news_list:
        message_str += f"Headline: {remove_non_ascii(news_dict['title'])}\n"
        message_str += f"Brief: {remove_non_ascii(news_dict['description'])}\n\n"

    create_news_file(message_str)
    print("Mail Send Successfully!!")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

