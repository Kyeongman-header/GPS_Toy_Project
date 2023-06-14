import requests
def get(num):
    response = requests.get("https://api.thingspeak.com/channels/2181834/fields/"+str(num)+".json?results=1")
    #?api_key=Q72D4G8BAREBH135
    # print(response)
    # print(response.json()['feeds'])

    data=response.json()['feeds']

    l=[] # filed 2 는 longitude.
    word='field'+str(num)
    l=data[-1][word]
    if l=='0.00':
        print("error on GPS module.")
        if num==1:
            print("서버 이상이 아니라 아두이노 gps가 langitude 0.00 좌표를 보내네요")
            print("기본 좌표 127.00으로 세팅합니다.")
            l=127.00
        else:
            print("서버 이상이 아니라 아두이노 gps가 longitude 0.00 좌표를 보내네요")
            print("기본 좌표 37.915로 세팅합니다.")
            l=37.915
    return l 

def update(data):
    response=requests.get("http://127.0.0.1:8000/update?longitude="+str(data['longitude'])+"&langitude="+str(data['langitude']))
    print(response.json())


import time
while True:
    now=time
    print("//////update.//////")
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(3) #3초동안 쉰다.
    
    last_langitude=get(1)
    last_longitude=get(2)
    update({'langitude' : last_langitude, 'longitude' : last_longitude})

