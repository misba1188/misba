from TwitterAPI import TwitterAPI

CONSUMER_KEY = 'IgeWqPZ4tExuq0vaBpUnDmZCh'
CONSUMER_SECRET = 'iVqr3xGlZU9ccizMAbrBiuPZB5SheYgYrnHXLhvbbs6g9yCfEw'
ACCESS_TOKEN_KEY = '910718686633246722-rCqXS80MF8H22x7CaIUohma7ME1F6rd'
ACCESS_TOKEN_SECRET = '	Y2Q0OpjZEdlQm5HbEW1h8IfA3ZV7CRtOdlmuxhqWi3g29'
b=1

while True:
    b=b+1
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    file = open('/home/pi/cam/imgs/'+str(b)+'.jpg', 'rb')
    print('done')
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':'#pyTweetCMR'}, {'media[]':data})
    print(r.status_code)