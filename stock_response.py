import requests

def res(stocks):
    key = '659bab86b16cf363cd3bd410816d3f82'
    ret = ""
    for stock in stocks:
        response = requests.get("http://api.marketstack.com/v1/intraday?access_key="+key+"&symbols="+stock+"&&limit=1")
        if response.status_code == 200:
            res = response.json()['data'][0]
            for key in res:
                temp = str(key)+"-> "+str(res[key])
                ret+= temp
                ret+="\n"
            ret+="_______________\n"
        else:
            continue
    return ret