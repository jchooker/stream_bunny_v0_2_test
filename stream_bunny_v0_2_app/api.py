import requests

url = "https://streaming-availability.p.rapidapi.com/search/basic"

querystring = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"1","output_language":"en","language":"en"}

headers = {
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com",
    'x-rapidapi-key': "9e6924077bmsh537baf971b723ddp1165e9jsn8c35b01cf3eb"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json)