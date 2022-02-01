import requests

# url = "https://streaming-availability.p.rapidapi.com/search/basic"

# querystring = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"1","output_language":"en","language":"en"}

# headers = {
#     'x-rapidapi-host': "streaming-availability.p.rapidapi.com",
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.json)

# {'hbo': {'us': {'link': 
# 'https://play.hbomax.com/page/urn:hbo:page:GXeOM3Q7qcZuAuwEAADwo:type:feature', 'added': 1609567234, 'leaving': 0}}}

def get_stream(imdb_id):

    url = "https://streaming-availability.p.rapidapi.com/get/basic"

    querystring = {"country":"us","imdb_id":f'tt{imdb_id}',"output_language":"en"}

    headers = {
        'x-rapidapi-host': "streaming-availability.p.rapidapi.com",
        'x-rapidapi-key': "9e6924077bmsh537baf971b723ddp1165e9jsn8c35b01cf3eb",  # Joseph's key
        # 'x-rapidapi-key': "2b0bb807b2msh8f81f82877e9118p17629cjsn1b5858449268", # Matthew's key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.json()["streamingInfo"])
    ret1 = response.json()["streamingInfo"]
    stream_arr = []
    for stream, value in ret1.items():
        stream_arr.append(
            {
                'stream':stream,
                'stream_link':value['us']['link']
                })
    return stream_arr

#/get/basic