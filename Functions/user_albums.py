def make_album(artist_name, album_title):
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    return album


while True:
    print('\nEnter artist name and album title')
    print('enter quit anytime when you want to quit')

    name = input('enter artist name')
    if name.lower() == 'quit':
        break

    title = input('enter album title')
    if title.lower() == 'quit':
        break

    album_info = make_album(name, title)
    print(album_info) 