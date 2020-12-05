import requests
import bs4 as bs
from urllib.parse import quote
import time

head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 \
        http://notifyninja.com/monitoring'}

def get_song_url(song):
    formatted_song = quote(song)
    url = 'http://www.google.com/search?q='+'+az+lyrics'+str(formatted_song)
    page = requests.get(url)
    soup = bs.BeautifulSoup(page.text, "lxml")
    # print(soup.find('cite').text)
    data = []
    for link in soup.find_all('a', href=True):
        if 'url' in link['href']:
            temp = link['href'].split('&')
            temp = temp[0].split('=')
            if "azlyrics" not in temp[1]:
                return False
            url = temp[1]
            break
    return url

def fetch(song):
    url = get_song_url(song)
    
    if not url:
        return False
    
    data = requests.get(url, headers=head)
    soup = bs.BeautifulSoup(data.text, "lxml")

    data = []
    for link in soup.find_all('div'):
        data.append(link.text)
    maxl = 0
    for d in data:
        if len(d) > maxl:
            dt = d
            maxl = len(d)
    for i in range(9):
        dt = dt.replace('\n\n', '\n')
    dt = dt.split('\n\r\n')
    
    data = ""
    for d in dt:
        if d.startswith("if"):
            break
        data += str(d)

    if data.strip().startswith("Welcome"):
        return False
    data = data.split("(")
    print("".join(data[0:]))
    return True

def get_lyrics(song):
    lyricsFound = fetch(song)

    if not lyricsFound:
        print("Lyrics not found :(")
		
    time.sleep(100)

get_lyrics(input("Enter Song name: "))
