import requests
res = requests.get('https://automatingtheboringstuff.com/files/rj.txt')
print(res.status_code)
len(res.text)
print(res.text[:500])
