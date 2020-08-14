import requests
from datetime import date
from bs4 import BeautifulSoup
today = date.today()
quotes=[]
url = "https://www.brainyquote.com/quote_of_the_day"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
view_quote  = soup.find_all(title="view quote")
print("########### QUOTE OF THE DAY - {}/{}/{} ###########\n".format(today.day,today.month,today.year))
for quote in view_quote:
	quotes.append(quote.text)
print(quotes[1])