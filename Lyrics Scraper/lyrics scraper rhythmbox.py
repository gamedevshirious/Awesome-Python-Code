import requests
import bs4 as bs
from urllib.parse import quote
# import urllib.request
# import os
import shlex
import subprocess
import re


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
    

def seperate(sym, string):
    if len(sym) == 1:
        string = string.split(sym)[0] if sym in string else string
    else:
        string = re.split('\\b" + str(sym) + "\\b', string)
    return string

'''
proc = subprocess.Popen(shlex.split(
        'rhythmbox-client --no-start \
        print-playing-format %aa-.-%tt'),
        stdout=subprocess.PIPE
                                    )

info, err = proc.communicate()
info = str(info, encoding="utf-8", errors="strict").split("-.-")

artistlist = seperate("-", info[0])
song = seperate("-", info[-1])

if len(artistlist) == 0 or len(song) == 0:
    artistlist, song = str(input("artist: ")), str(input("song: "))


for sym in "', '&|":
    try:
        print(sym)
        for sym in artistlist:
            artist = artistlist.split(sym)
            print(artist)
    except Exception as e : break

artist = artistlist.split(",")[0]
artist = artist.split("feat.")[0]  # .rstrip("feat")
'''

# artist, song = str(input("artist: ")), str(input("song: "))

artist = "sIa"
song = "cheap+thrills"

# lyricsFound = fetch(artist, song)
#print(lyricsFound)
lyricsFound = fetch(song)
if not lyricsFound:
    artists = ["Bollywood","Bangtan Boys"]
    for artist in artists:
        #lyricsFound = fetch(artist, song)
        if lyricsFound: 
            break
if not lyricsFound:
    print("Lyrics not found :(")
'''
flag = 1
while(flag == 1 and len(artist) >= 0):
    flag = fetch(artist,song)
    #artist.pop(0)
'''
