import requests
url = 'https://ve48.aadika.xyz/download/7vBL2JF6SdI/mp3/128/1670664093/d9bdddd77c552b202a7b224cba4aa588633dd7e0c1857ba237703162364ed91e/1?f=yt5s.com'
r = requests.get(url, allow_redirects=True)
open('facebook.mp3', 'w+').write(r.content)

