import requests

# r = requests.post("http://www.amazon.com", data={'number': '12524', 'type': 'issue', 'action': 'show'})
r = requests.post("https://bugs.python.org")
#print('The status code is ', r.status_code)
print(r.text[:300] + '...')