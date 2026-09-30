import requests
import datetime
import os 
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()
import spotipy
import re
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt" 
    )
)
user_id = sp.current_user()["id"]
print(f"Successfully authenticated as User ID: {user_id}")

while True:
    teleport_date = input("Enter the date you want to teleport to in YYYY-MM-DD FORMAT : ")
    try:
        valid_date = datetime.datetime.strptime(teleport_date, "%Y-%m-%d")
        break
    except ValueError:
        print("INVALID FORMAT, KINDLY ENTER IN YYYY-MM-DD FOMRAT")

def nearest_friday():
    
    current_week_day = valid_date.weekday()
    days_to_friday = 4 - current_week_day
    friday_date = valid_date.date() + datetime.timedelta(days= days_to_friday)
    return friday_date

target_date = nearest_friday()
date_for_url = str(target_date)
final_date = date_for_url.replace("-","")


my_headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
    "Accept-language" : "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
repsonse = requests.get(url= f"https://www.officialcharts.com/charts/singles-chart/{final_date}/7501/", headers= my_headers)
repsonse.raise_for_status()
soup = BeautifulSoup(repsonse.text, "html.parser")
track_elemets = soup.select(".chart-name")
track_list=[]
for track in track_elemets:
    track_title = track.get_text(strip = True)
    track_title = re.sub(r"^(New|Re)", "", track_title)
    track_list.append(track_title)
    
artist_name = []
artist_element = soup.select(".chart-artist")
for artist in artist_element:
    artist_title = artist.get_text(strip = True)
    final_title = artist_title.replace("/",",")
    artist_name.append(final_title)
    

tracks_uri = []
for track, artist in zip(track_list, artist_name):
    primary_artist = artist.split(" FT ")[0].split(" & ")[0]
    query = f"{track} {primary_artist}"
    result = sp.search(q=query, type="track", limit=1) 
    
    try:
        uri = result["tracks"]["items"][0]["uri"]
        tracks_uri.append(uri)
    except(KeyError, IndexError):
        print(f"Skipped {track} by {artist}, could not be found on spotify")

playlist_name = f"{teleport_date} Chart Toppers"
playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=f"Top UK singles chart hits for week of {teleport_date}."
)

if tracks_uri:
    sp.playlist_add_items(playlist_id=playlist["id"] , items = tracks_uri)
    print(f"Successfully created playlist '{playlist_name}")
else:
    print("No valid uris found to fill the playlist")                
        
   


    

    
    

