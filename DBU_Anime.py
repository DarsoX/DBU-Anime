import http.client

conn = http.client.HTTPConnection("EROR_ROT")

def get_topanime(years = 2020):
    conn.request("GET", "/aimedbu?method=get_topanime&year={}".format(years))

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

def get_anime():
    conn.request("GET", "/aimedbu?method=get_anime")

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

def get_animejanr(janr = ''):
    if janr != '':
        onn.request("GET", "/aimedbu?method=get_animejanr&janr={}".format(janr))

        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")
    else:
        return 'DBU_EROR: Укажите Жанр.'
