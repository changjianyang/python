import urllib.request


for num in range(0, 500):
    url = 'http://localhost:11003/mana/getport'
    req = urllib.request.Request(url)
    data = urllib.request.urlopen(req).read()
    print(data, '-->' , num)