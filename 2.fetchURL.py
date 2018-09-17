import requests
r =requests.get('https://api.thingspeak.com/channels/573086/feeds.json?api_key=1135FZD12JH7HP5P&results=1')
print r.text
