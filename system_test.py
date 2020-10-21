import requests
import time
import json
import hashlib
api = "http://localhost:9000"

r1 = requests.post(api + "/login", verify=False)
print(r1.text)

r2 = requests.post(api+"/connect", verify=False)
print(r2.text)

r3 = requests.post(api+"/query", verify=False)
print(r3.text)

r4 = requests.post(api+"/insert", verify=False)
print(r4.text)

r5 = requests.post(api+"/getOrgs", verify=False)
print(r5.text)

r6 = requests.post(api+"/transfer", verify=False)
print(r6.text)

r7 = requests.post(api+"/history", verify=False)
print(r7.text)

r8 = requests.post(api+"/allAsset", verify=False)
print(r8.text)

print("Next test will start after 5 seconds...")
time.sleep(5)

passwd = "12345678"
m = hashlib.md5()
m.update(passwd.encode("utf-8"))
h = m.hexdigest()

r9 = requests.post(api+"/connect", json={
    "username": "newUser",
    "password": h
})
print(r9.text)
data = json.loads(r9.text)
if (data['code'] == 0):
    r10 = requests.post(api+"/query", json={
        "token":  data['token'],
        "key": "123"
    })
    print(r10.text)
