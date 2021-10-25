import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name":"nyash","likes":11, "views":113},
    {"name":"paul","likes":1, "views":13},
    {"name":"trump","likes":21331, "views":879001},
    {"name":"cool","likes":1, "views":13},
    {"name":"investing","likes":1222, "views":13003},
    {"name":"oven baked rice","likes":112221, "views":2830000}
]

for i in range(len(data)):
    #update with new video data
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

response = requests.delete(BASE + "video/0")
print(response)
input()

#get the data if all the required arguments are given
response = requests.get(BASE + "video/5")
print(response.json())