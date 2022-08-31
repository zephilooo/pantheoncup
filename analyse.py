import requests
from bs4 import BeautifulSoup

url = "https://zephilooo.github.io/"
res = requests.get(url)

if res.ok:
    soup = BeautifulSoup(res.text,'lxml')
    line_c = soup.findAll('tr',{'class' : 'papi_liste_c'})
    line_f = soup.findAll('tr',{'class' : 'papi_liste_f'})
    lines = [line.text for line in line_c] + [line.text for line in line_f]
    for l in lines:
        new_l = l.splitlines()
        print("A la table {}, {} joue avec les blancs contre {}".format(new_l[1],new_l[3],new_l[6]))
