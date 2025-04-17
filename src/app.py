import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

#TODO 5: Make APi requests

# Fav artist ID
result = spotify.search(q='Tiesto', type='artist')
artist_id = result['artists']['items'][0]['id']

# artist track
top_tracks = spotify.artist_top_tracks(artist_id)['tracks']

songs_data = []

for track in top_tracks[:10]:
    name = track['name']
    popularity = track['popularity']
    duration_ms = track['duration_ms']
    duration_min = round(duration_ms / 60000, 2)

    songs_data.append({
        'name': name,
        'popularity': popularity,
        'duration_min': duration_min
    })

#TODO #6: Transform to PD DataFrame
df = pd.DataFrame(songs_data)
sorted_df = df.sort_values(by='popularity')
print(sorted_df.head(3))  # Bottom 3 by popularity

#TODO #7 Analysis statistical relationship
plt.figure(figsize=(8, 5))
plt.scatter(df['duration_min'], df['popularity'], color='purple')

plt.title('Song Duration vs Popularity')
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')

plt.grid(True)
plt.show()


# Note to Samir. The graph won't load in the terminal for some reason. I ran it in a Jupyter notebook and it worked perfectly.
print("Conclusion:\n His most popular song is one of the shortest songs of his. Most of his songs range between 2.5 and 3.0 minutes in duration.")