import requests
import json
api_url_login = "https://pythontest2021.azurewebsites.net/api/Login"
api_url_fa = "https://pythontest2021.azurewebsites.net/api/Get2FACode/"
user= input("Unesite usera: ")
lozinka = input("Unesite lozinku: ")
data = {"username": user, "password": lozinka}
json_data = json.dumps(data)
headers = {'Accept': 'text/plain', 'Content-Type': 'application/json'}



code= input("Unesite Kod sa ekrana: ")
print("Unijeli ste kod:", code, "Šaljem na Login Url")
if not code:
   raise ValueError("kod ne može biti nula")
else:
    data3 = {"username": user, "password": lozinka, "code": code }
    json_data = json.dumps(data3)
    response3 = requests.post(api_url_login, headers=headers, data=json_data)
    #Token = data["token"]
    print(response3.text)
