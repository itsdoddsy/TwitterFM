import twitter, config, requests, time, os, json

start = time.time()

SHORTENER_BASE = 'https://www.googleapis.com/urlshortener/v1/url'
api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.COMSUMER_SECRET,
                  access_token_key=config.ACCESS_KEY,
                  access_token_secret=config.ACCESS_SECRET)


def get_short_url(url):
    data = {'longUrl': url}
    params = {'key': config.SHORTENER_API_KEY}
    headers = {'content-type': 'application/json'}
    response = requests.post(SHORTENER_BASE, params=params,
                             data=json.dumps(data), headers=headers)
    return response.json()["id"]


def get_lastfm_request(method, **kwargs):
    return requests.get(LASTFM_API_URL, params={"method": method,
                                                **REQUEST_PARAMETERS,
                                                **kwargs})


def parse_tags(response):
    for tag in response.json()['toptags']['tag'][:3]:
        tag_name = tag['name']
        if tag_name in ('seen live',):
            continue
        yield tag_name.lower()


def read_cache():
    return open(config.SONG_CACHE, 'r').read()


LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
REQUEST_PARAMETERS = {'api_key': config.LASTFM_KEY, 'format': 'json'}

if __name__ == "__main__":
    if os.path.isfile(f'./{config.SONG_CACHE}'):
        print(f'Found song cache file \'{config.SONG_CACHE}\'')

    else:
        print(f'Song cache file \'{config.SONG_CACHE}\' doesn\'t exist, will be created in current directory')

    while True:
        latest_track = get_lastfm_request("user.getRecentTracks",
                                          user=config.LASTFM_USERNAME, limit=1).json()["recenttracks"]["track"][0]

        # specify track and artist info as well as last.fm tags
        artist = latest_track["artist"]["#text"]
        tag_response = get_lastfm_request("artist.getTopTags", artist=artist)
        tags = ', '.join(parse_tags(tag_response))
        tags_or_no = f"\nTags: {tags}" if tags else ''
        # get goo.gl url to last.fm track page
        link = get_short_url(latest_track["url"])

        # set message to post to twitter
        nowplaying = f'''#nowplaying {json.dumps(latest_track["name"], ensure_ascii=False)} by {json.dumps(latest_track["artist"]["#text"], ensure_ascii=False)} {tags_or_no}\n{link}'''

        if read_cache() != json.dumps(latest_track):
            with open(config.SONG_CACHE, 'w') as f:
                json.dump(latest_track, f)
            print(nowplaying)
            if not latest_track["image"][2]["#text"] == '':
                api.PostMedia(
                    status=nowplaying,
                    media=latest_track["image"][2]["#text"]
                )
            else:
                api.PostUpdate(nowplaying)

        time.sleep(int(config.UPDATE_TIME) - ((time.time() - start) % int(config.UPDATE_TIME)))
