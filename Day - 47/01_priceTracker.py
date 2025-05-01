from bs4 import BeautifulSoup
import requests
import smtplib
import Dummy

response = requests.get("https://www.amazon.com.au/Harry-Potter-Complete-Collection-Boxset/dp/1408856778/ref=sr_1_1?crid=2IHYJR0E67I9J&dib=eyJ2IjoiMSJ9.eSzvr7PfPStp43yLtyh0KJ4wReC2oaMvV_txU7SwYA2LYt9atQSTwMQbY1VojRjNs_Z71G1s5eiQIws8YYuXJ0SDhBPpLBI9Q69lMQVS2yZfKF_hVx6sT0pai1ZHm-g88HprUghFW_r-QDSGdxNWdkSLP0Qr7s5nrg8UVFyG-4rZwBTLRQ7qs9cGfoH6FjJoBxiu9KE3vW4aTjSSkBMNR_qLdsCF9DKmJe3lJvZwJKOianMdxQQ3vTKOpj6GN4-cTb6vdoAbkc2b8IynOGbKlqUDQLs1NjQnacpwvzPjQ1g.O9zqyQOO4Dp-JgyECdlYOPG30YMgyk5VpD9HUMZI60Q&dib_tag=se&keywords=harry+potter+books&qid=1746126116&sprefix=harry+potter+book%2Caps%2C378&sr=8-1")
response.raise_for_status()
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")

price = soup.find(name='span', id='a-price-whole')
print(price)


if int(price) < 50 :
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=Dummy.MY_EMAIL, password=Dummy.MY_PASS)
        connection.sendmail(
            from_addr=Dummy.MY_EMAIL,
            to_addrs=Dummy.TO_EMAIL,
            msg=f"Subject : Low Price Alert on Amazon Items!! \n\n Current Price is {price}"
        )
