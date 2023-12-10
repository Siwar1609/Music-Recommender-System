from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

client_id = 'c86e60558b4c46249c2d7bf48d6edf7d'
client_secret = '2559d19136634386bdeb3a6b55e7679b'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

data = pd.read_csv('final_dataset.csv')
tv = TfidfVectorizer(analyzer='word', stop_words='english')
vec = tv.fit_transform(data['specifity'])
similarity = pickle.load(open('similarity.pkl', 'rb'))


    
    
    
def get_spotify_link(track_name):
    result = sp.search(q=track_name, type='track')

    #check if there are search results
    if result['tracks']['items']:
      
        track = result['tracks']['items'][0]
        
        spotify_link = track['external_urls']['spotify']
        return spotify_link
def get_album_cover_url(track_name):
    result = sp.search(q=track_name, type='track', limit=1)
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        #extraire l'url 
        album_cover_url = track['album']['images'][0]['url']
        return album_cover_url
def recommend(song):
    if song in data['track_name'].unique():
        song_index = data[data['track_name'] == song].index[0]
        distances = similarity[song_index]
        song_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:5]
        recommended_songs = []

        for i in song_list:
            track_name = data.iloc[i[0]]['track_name']
            spotify_link = get_spotify_link(track_name)
            album_cover_url = get_album_cover_url(track_name)
            recommended_songs.append({
                "track_name": track_name,
                "spotify_link": spotify_link,
                "album_cover_url": album_cover_url
            })

        return recommended_songs

@app.route('/')
def index():
    track_names = data['track_name'].unique()
    return render_template('template.html', track_names=track_names, recommendation_items=data.to_dict(orient='records'))

@app.route('/content_recommendations',methods=['GET'])
def content_recommendations():
    track_name = request.args.get('track_name')
    recommendations = recommend(track_name)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)

