import requests
import json
import time

token = ''
#einlesen des Tokens
fobj = open("token.dat")
for line in fobj:
	token = line.rstrip()
fobj.close()


headers = {'Content-Type':'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
root = 'https://www.intern-e.evlka.de/toro/api/v1/'

data = {'message':'Diese Nachricht wurde über Python an Intern-E verschickt.'}
id = 'CONVERSATION%2C21956'
command1 = 'conversation/'
command2 = '/message'


def post(data, id, command1, command2):
    command = command1 + id + command2
    url = root + command
    resp = requests.post(url, json.dumps(data), None, headers=headers)
    if resp.status_code != 200:
        # This means something went wrong.
        print(resp.status_code)
    print(resp.json())


start = time.time()
post(data, id, command1, command2)
ende = time.time()
print('{:5.3f}s'.format(ende - start))
data={'message':'Diese Nachricht hat '+'{:5.3f}s'.format(ende - start)+' zum Senden gebraucht.'}
post(data,id,command1,command2)
# curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'Authorization: Bearer 09f116f7-7e97-4fe6-b006-731689e57d9e' -d '{"message":"Diese Nachricht wurde über die Intern-E-API gesendet."}' 'https://www.intern-e.evlka.de/toro/api/v1/conversation/CONVERSATION%2C21956/message'
