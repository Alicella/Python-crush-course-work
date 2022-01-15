from re import A, T


def make_album(artist, title, track=''):
    album = {'Artist': artist.title(), 'Title': title.title()}
    if track:
        album['Track'] = track
    return album

# example1 = make_album('adel', '30', track='9')
# example2 = make_album('bob dylan', 'blowing in the wind')
# print(example1)
# print(example2)

while True:
    print("\nenter q anytime to quit.")
    artist = input("Artist Name: ")
    if artist == 'q':
        break
    title = input("Album title: ")
    if title == 'q':
        break
    track = input("Album track # (optional): ")
    if track == 'q':
        break
    
    example = make_album(artist, title, track)
    print(example)