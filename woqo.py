import requests
from datetime import date
from bs4 import BeautifulSoup
today = date.today()
try:	
	with open("woqo.txt", 'r') as f:
		line = f.readlines()[-1]
	count = int(line[0])

except FileNotFoundError:
	count = 1
url = "https://www.brainyquote.com/quote_of_the_day"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
view_quote  = soup.find_all(title="view quote")
with open("woqo.txt","a") as file:
	file.write("########### QUOTE OF THE DAY - {}/{}/{} ###########\n".format(today.day,today.month,today.year))
	for quote in view_quote:
		file.write("{} {} {}".format(count,quote.text,"\n"))
		count = count+1
