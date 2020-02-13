# if package is gone missing, 빨간 줄 그어있는걸 보고 alt+ Enter 를 친다

def get_song_naver(num):
    import requests
    import bs4
    url = 'https://music.naver.com/'
    header = {'user-agent':
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    response = requests.get(url, headers=header)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    ranking = soup.select('tr._track_dsc')
    # print(ranking[0])

    # rank = ranking[0].select_one('td.ranking span')
    # artist = ranking[0].select_one('td.artist a')
    # title = ranking[0].select_one('td.name a')

    ranks = []
    for song in ranking[:num]:
        rank = song.select_one('td.ranking span')
        artist = song.select_one('td.artist a')
        title = song.select_one('td.name a')
        # print(rank.text)
        # print(title.text)
        # print(artist.text)
        info = {
            'rank': rank.text,
            'title': title.text,
            'artist': artist.text
        }
        # print(info)
        ranks.append(info)
    return ranks


