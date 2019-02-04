
opera = {
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
#print(opera['visitatore']['opere'][0])

#----
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


URL = 'http://127.0.0.1:8080/'

SensorID = 'FFF6Y6Y688J'
#newURL = URL + SensorID
payload = {'sensorID': 'CCCT67677BB'}
URLL = URL + 'artwork_info'
sec =0.00
for i in range(1,1000):
    r1 = s.get(URLL, params=payload).elapsed.total_seconds()
    sec = sec + r1.real
    print(i, r1, float(sec/i))

#print(r1.text)