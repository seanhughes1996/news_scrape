
# %% Imports
from bs4 import BeautifulSoup
import requests

urls = [r'https://www.bbc.co.uk/news', 
       r'https://edition.cnn.com/', 
       r'https://www.dailymail.co.uk/home/index.html', 
       r'https://www.independent.co.uk/'
       ]


f = open(r'C:\projects\news_scrape\Enviroments\web_scrape\Scripts\output.txt', 'w+')
for url in urls:
    r    = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    tag        = 'title'
    title_soup = soup.find(tag)
    
    f.write("{}\n".format(title_soup.string))

f.close()    


    
# %%