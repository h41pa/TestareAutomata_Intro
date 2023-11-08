import requests

# Setează valorile tale
client_id = "---"
client_secret = "------------"
user_id = "----------"
access_token = "-----"
# Creează playlist-ul
create_playlist_endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

playlist_data = {
    "name": "Nume Playlist",
    "description": "Descriere Playlist",
    "public": True
}

response = requests.post(create_playlist_endpoint, headers=headers, json=playlist_data)

if response.status_code == 201:
    print("Playlist creat cu succes!")
    playlist_id = response.json()["id"]
    print(f"ID-ul playlist-ului creat este {playlist_id}")
else:
    print("Eroare la crearea playlist-ului:", response.status_code, response.text)
