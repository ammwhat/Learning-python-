import requests
from bs4 import BeautifulSoup
letterbox_url = "https://letterboxd.com/official/list/top-250-films-with-the-most-fans/"
my_headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
    "Accept-language" : "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
response = requests.get(url = letterbox_url, headers = my_headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

movie_posters = soup.select(".film-poster img")
for poster in movie_posters:
    title = poster.get("alt")
    with open("movies.txt" , 'a') as f:
        f.write(f"{title}\n")
           
