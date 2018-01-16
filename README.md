# TwitterFM
Post current last.fm song to Twitter

## 1. Initial setup
1. `pip install -r requirements.txt`
2. Copy `config.py.empty` to `config.py`

## 2. Last.fm setup
1. Create an account @ https://www.last.fm/
2. https://www.last.fm/api/account/create
3. Fill out application name. All other fields aren't necessary.
4. Copy your API key
5. Put it in the single quotes for `LASTFM_KEY` in `config.py`
6. Put your Last.fm username in the single quotes for `LASTFM_USERNAME` in `config.py`

## 3. Twitter setup
<sup>**Note: creating a new account for this is recommended but optional**</sup>
1. Go to https://apps.twitter.com/ and create a new app
2. Fill out the required fields (for Website insert your full Twitter page url - `https://twitter.com/`**`username`**)
3. Tick the Developer Agreement checkbox and hit create
4. In the `Keys and Access Tokens` tab, scroll down and hit "Create my access token"
5. Insert your Consumer Key into `CONSUMER_KEY`, Consumer Secret into `CONSUMER_SECRET`, Access Token into `ACCESS_KEY` and Access Token Secret into `ACCESS_SECRET`

## 4. URL Shortener setup
1. Go to https://developers.google.com/url-shortener/v1/getting_started#APIKey and hit `Get a key`
2. Create a new project or use an existing project
3. Insert your API key into `SHORTENER_API_KEY`

bobs your uncle

## Running
**(Make sure you have Python 3.6 installed before doing this)**    
`python main.py`

If `python` runs a different version:
`python3.6 main.py`
