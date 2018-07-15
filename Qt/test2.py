import json


user = {}
user ['pathum'] = {

'user_id' : 'pm30',
'type' : 'admin',
'action' : 'log in',

}

user ['madushan'] = {

'user_id' : 'kk3250',
'type' : 'manager',
'action' : 'add user',
}


ob = json.dumps(user)
# print (ob)

ob = json.dumps (user)
with open ("C://Users//Pathum//Desktop//wri.txt", "w") as f:

    f.write(ob)

f =  open ("C://Users//Pathum//Desktop//wri.txt", "r")
ob = f.read()
# print (ob)

# convert string into dict
user = json.loads(ob)
print (user)
# typeof =  type (user)
# print (typeof)

acces = user ['pathum'] ['action']
print (acces)

acces2 = user ['madushan'] ['action']
print (acces2)