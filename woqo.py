import requests
from datetime import date
from bs4 import BeautifulSoup
today = date.today()
quotes=[]
td = today.day
tm = today.month
ty = today.year
### DICTIONARY.COM ###

print(r'''
	
__        __           ___          
\ \      / /   ___    / _ \    ___  
 \ \ /\ / /   / _ \  | | | |  / _ \ 
  \ V  V /   | (_) | | |_| | | (_) |
   \_/\_/     \___/   \__\_\  \___/ 
          @github.com/iam-shanmukha/

	''')

word = "https://www.dictionary.com/e/word-of-the-day/"
word_page = requests.get(word)
word_soup = BeautifulSoup(word_page.content,'html.parser')
view_word = word_soup.find('title')
view_word_def  = word_soup.find("div", {"class": "otd-item-headword__pos-blocks"})

### BRAINYQUOTE.COM ###
brainyquote = "https://www.brainyquote.com/quote_of_the_day"
brain_page = requests.get(brainyquote)
brain_soup = BeautifulSoup(brain_page.content, 'html.parser')
view_quote  = brain_soup.find_all(title="view quote")
#class="otd-item-headword__pos-blocks"

print("########### WORD OF THE DAY - {}/{}/{} ###########\n".format(td,tm,ty))
print(view_word.string[18:-16].strip())
print(view_word_def.text.strip())
print()
print("########### QUOTE OF THE DAY - {}/{}/{} ###########\n".format(td,tm,ty))
for quote in view_quote:
	quotes.append(quote.text)
print(quotes[1])