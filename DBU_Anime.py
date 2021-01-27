import json
import requests

def get_topanime(years = 2020):
    
    get_topanimes = requests.get('https://dbuapi.herokuapp.com/aimedbu?method=get_topanime&year={}'.format(years)).json()
    
    return json.loads(get_topanimes)


def get_anime():
    
    get_animes = requests.get('https://dbuapi.herokuapp.com/aimedbu?method=get_anime').json()
    
    return json.loads(get_animes)

def get_animejanr(janr = ''):
    if janr != '':
        
        get_animejanrs =requests.get('https://dbuapi.herokuapp.com/aimedbu?method=get_animejanr&janr={}'.format(janr))
        
        return json.loads(get_animejanrs)
    else:
        return 'DBU_EROR: Укажите Жанр.'
