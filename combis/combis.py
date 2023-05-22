import requests
import json
api_url_login = "https://pythontest2021.azurewebsites.net/api/Login"
api_url_fa = "https://pythontest2021.azurewebsites.net/api/Get2FACode/"
user= input("Unesite usera: ")
lozinka = input("Unesite lozinku: ")
data = {"username": user, "password": lozinka, "code": "" }
json_data = json.dumps(data)
headers = {'Accept': 'text/plain', 'Content-Type': 'application/json'}
response1 = requests.post(api_url_login, headers=headers, data=json_data)
if  response1.status_code == 200:
    data = response1.json() 
else:
    print("Naletio sam na error i izlazim iz aplikacije!")
    exit()
if not data['is2FAEnabled']:
    Token = data["token"]
    print("token koji tražite je:", Token)
    exit() 
if data['is2FAEnabled']:
    response2 = requests.post(api_url_fa, headers=headers, data=json_data)
    print(response2.text)
code= input("Unesite Kod sa ekrana: ")
print("Unijeli ste kod:", code, "Šaljem na Login Url")
if not code:
   raise ValueError("kod ne može biti nula")
else:
    data3 = {"username": user, "password": lozinka, "code": code }
    json_data = json.dumps(data3)
    response3 = requests.post(api_url_login, headers=headers, data=json_data)
    if  response3.status_code == 200:
        data = response3.json()
        Token = data["token"]
        print("token koji tražite je:", Token)
    else:
        print("Naletio sam na error i izlazim iz aplikacije!")
        exit()
