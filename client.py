import requests 

add_new_resp = requests.post('http://127.0.0.1:8000/colors', json={'name':'purple'})
print(add_new_resp.text)

resp = requests.get('http://127.0.0.1:8000/colors').json()
print(resp)

for c in resp:
    print (c)
