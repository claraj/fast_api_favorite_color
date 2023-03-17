import requests 

add_new_resp = requests.post('http://127.0.0.1:8000/api/colors', json={'name':'orange'})
print(add_new_resp.text)

resp = requests.get('http://127.0.0.1:8000/api/colors').json()
print(resp)

for c in resp:
    print (c)

resp = requests.delete('http://127.0.0.1:8000/api/admin_color_delete')
