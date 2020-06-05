#Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.

def make_sandwich(*sandwiches):
    print('\nThis are the sandwiches that we have: ')
    for sandwich in sandwiches:
        print("-" + sandwich)

make_sandwich('tuna')
make_sandwich('tuna','pastrami')
make_sandwich('blt', 'pastrami', 'cheese')


def build_profile(first, last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        
    return profile
user_profile = build_profile('matheus', 'dantas', age='29', nationality='brazilian', height='1,84')
print(user_profile)


def make_album(artist,title, tracks = ''):
    if tracks:
        album = {'artist' : artist, 'title' : title, 'tracks' : tracks}
    else:
        album = {'artist' : artist, 'title' : title}
    return album
music_album = make_album('slipknot','IOWA')
print(music_album)
music_album = make_album('Linkin Park','Meteora','13')
print(music_album)
music_album = make_album('Pitty','Anacronico')
print(music_album)
