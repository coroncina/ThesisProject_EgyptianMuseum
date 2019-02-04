import requests
import json

"""json
{
    'visitatore': {
        'id_visitatore': 'CarlaC',
        'opere': [
            {'opera': {
                'id_opera': 'Cat.8888',
                'tempo_impiegato': 98,
                'apprezzamento': 1,
                'info_ricevute': 1 }
            }
        ]
    }
}
"""

s=requests.session()

#r = s.get('http://127.0.0.1:8080/')
#print(r.status_code)

#r = s.post('http://127.0.0.1:8080/')
#print(r.status_code, r.text)

#json_received = json.dumps(r.text)
#print(json_received)

## ------------------------------------ client definitivo x provare upload in mongo --------------------------------- ##

json_data = {'visitatore':{'id_visitatore':'CarlaC','opera':{'id_opera':'Cat.9898','tempo_impiegato':333,'apprezzamento':5}}}
json_data1 = {'visitatore':{'id_visitatore':'CarlaC','opere':[{'opera':{'id_opera':'Cat.1111','tempo_impiegato':2,'apprezzamento': 1,'info_ricevute':1}}]}}

URL = 'http://127.0.0.1:8080/'

#scommenta se vuoi testare

#r = requests.post(URL, data=json.dumps(json_data1))
#print(str(r.content))
#print(r.text)

## ------------------------------------------------------------------------------------------------------------------ ##


## ------------------------------------------------------------------------------------------------------------------ ##
##------ nuova prova per mandare richiesta iniziale con id del sensore quindi costruisco una get con URL/SensorID

SensorID = 'CCCT67677BB'
#newURL = URL + SensorID
payload = {'sensorID': 'CCCT67677BB'}
URLL = URL + 'artwork_info'
sec=0.00
for i in range(1,2):
    r1 = requests.get(URLL, params=payload)#.elapsed.total_seconds()
    #sec = sec + r1.real
    #print(i, r1, float(sec/i))

    print(r1.text)
