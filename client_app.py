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

json_data = {'visitatore':{'id_visitatore':'CarlaC','opera':{'id_opera':'Cat.9898','tempo_impiegato':333,'apprezzamento':5}}}
json_data1 = {'visitatore':{'id_visitatore':'ELISABETTA','opere':[{'opera':{'id_opera':'Cat.1111','tempo_impiegato':2222,'apprezzamento': 1,'info_ricevute':1}}]}}

URL = 'http://127.0.0.1:8080/'
r = requests.post(URL, data=json.dumps(json_data1))

print(str(r.content))
print(r.text)
