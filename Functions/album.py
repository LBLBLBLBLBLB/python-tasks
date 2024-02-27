def make_album(artist_name, album_title, song_count=None):
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if song_count:
        album['song_count'] = song_count
    return album


album1 = make_album('A B', 'C D', 10)
album2 = make_album('Name', 'Title')
album3 = make_album('Another Artist', 'Another Album', 15)

print(album1)
print(album2)
print(album3)