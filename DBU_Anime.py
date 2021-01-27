import json
from request import get

def get_topanime(years = 2020):
    
    get_top = request.get('')
    
    return 

def get_anime():
    
    get_animes = get('https://dbuapi.herokuapp.com/aimedbu?method=get_anime').json()
    
    return json.loads(get_animes)

def get_animejanr(janr = ''):
    if janr != '':
        onn.request("GET", "/aimedbu?method=get_animejanr&janr={}".format(janr))

        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")
    else:
        return 'DBU_EROR: Укажите Жанр.'
