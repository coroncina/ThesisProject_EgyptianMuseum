from pymongo import MongoClient

client = MongoClient('localhost', 27017)
print(client.database_names)

db = client['visitorProfileDB'] #CREO UN NUOVO DB

#ORA VOGLIO CREARE UNA COLLEZIONE
visitor_profiles = db.visitorProfiles
print(visitor_profiles)

#NOW I WILL CREATE THE DOCUMENT TO BE INSERTED INSIDE THE COLLECTION OF THE DB
visitor = {
    'visitatore': {
        'id_visitatore': 'CarlaC',
        'opere': [
            {'opera': {
                'id_opera': 'Cat.7777',
                'tempo_impiegato': 98,
                'apprezzamento': 1,
                'info_ricevute': 1 }
            }
        ]
    }
}
id_user = visitor["visitatore"]["id_visitatore"]
opera = visitor["visitatore"]["opere"][0]
#results = visitor_profiles.insert_one(visitor)
#print(results)

found=0
for visit in visitor_profiles.find({'visitatore.id_visitatore':visitor['visitatore']['id_visitatore']}):
    #se uguale, fai check opera
    #NB: entra qui dentro solo se lo trova!!!
    found = 1
    visitor_profiles.update(
        {'visitatore.id_visitatore': id_user},
        {"$addToSet": {'visitatore.opere': opera}})

if (found==0):
    #THIS MEANS THAT IS A NEW VISITOR ARRIVED
    print(found)
    #se il visitor non è nel db significa che dobbiamo aggiungerlo
    res = visitor_profiles.insert_one(visitor)
    print("nuovo visitatore")

#if results.acknowledged:
#    print("Visitor Added. The visitor Id is: " + str(results.inserted_id))

"""
play with queries
"""
# ------------- find_one()
#x = visitor_profiles.find_one()
#print(x)

# -------------- find()
#for x in visitor_profiles.find({'visitatore.id_visitatore': "CarlaC"}):
#  print(x)

# -------------- delete_one()
#del_element = {"visitatore.id_visitatore": "LorenzoR"}
#visitor_profiles.delete_one(del_element)

# new_opera = {
#             "opera": {
#                 "id_opera": "Cat.7777",
#                 "tempo_impiegato": 777,
#                 "apprezzamento": 777,
#                 "info_ricevute": 777
#             }
# }
#
# #The first thing to do when a new POST request arrives from the client, we have to check if the user is already in the db, so
# id_user = visitor["visitatore"]["id_visitatore"]
# #print(id_user)
# for visit in visitor_profiles.update(
#          {'visitatore.id_visitatore': id_user},
#          {"$addToSet": {'visitatore.opere': new_opera}} ):
#     print(str(visit))

