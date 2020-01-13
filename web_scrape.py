
# %% Imports
from bs4 import BeautifulSoup
import requests
import os

urls = [r'https://www.bbc.co.uk/news', 
       r'https://edition.cnn.com/', 
       r'https://www.dailymail.co.uk/home/index.html', 
       r'https://www.independent.co.uk/'
       ]

currentDirectory = os.getcwd()
f = open(currentDirectory + '\output.txt', 'w+')
for url in urls:
    r    = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    tag        = 'title'
    title_soup = soup.find(tag)
    
    f.write("{}\n".format(title_soup.string))

f.close()    


    
# %%