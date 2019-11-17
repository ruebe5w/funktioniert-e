import requests
import json
import time
import mysql.connector

#variable
token = ''
wiederholungen = 10
times = []

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

#Array zur wiederholten Anwendung
for x in range(wiederholungen): 
	start = time.time()
	post(data, id, command1, command2)
	ende = time.time()
	usedTime = ende - start
	times.append(usedTime)




print('{:5.3f}s'.format(ende - start))
data={'message':'Diese Nachricht hat '+'{:5.3f}s'.format(ende - start)+' zum Senden gebraucht.'}
post(data,id,command1,command2)
# curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'Authorization: Bearer 09f116f7-7e97-4fe6-b006-731689e57d9e' -d '{"message":"Diese Nachricht wurde über die Intern-E-API gesendet."}' 'https://www.intern-e.evlka.de/toro/api/v1/conversation/CONVERSATION%2C21956/message'

#DB einschreiben des Datensatzes
dbconnect = mysql.connector.connect(
	host='sql133.your-server.de',
	database='kitppp_db1',
	user='kitppp_1_w',
	password='eDSTM7AHMFzJa7nM'
)
dbcursor = dbconnect.cursor()

for x in range(wiederholungen):
	sql = "INSERT INTO INTERNEEVLKA (datetime,type, runtime) VALUES(%s, %s)"
	val = (time.strftime('%Y-%m-%d %H:%M:%S'), "group-message", times[x]*100)
	dbcursor.execute(sql, val)




dbconnect.commit()
print(dbcursor.rowcount, "record inserted.")