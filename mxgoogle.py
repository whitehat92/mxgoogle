import spf
import sys
import DNS
import requests
import bs4
from bs4 import BeautifulSoup as bs

datainput = sys.argv[1]
url = "https://toolbox.googleapps.com/apps/checkmx/check?domain=" + datainput + "&dkim_selector="
headers = {'User-agent': 'Mozilla//10.0',}
conteudo = requests.get(url, headers=headers)
titles = bs(conteudo.content, "lxml").get_text()
titssanitized = titles.replace("\n", " ")
print(titssanitized)
