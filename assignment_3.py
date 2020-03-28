# Practice 1


import requests

url = "https://en.wikipedia.org/wiki/main_page"
res = requests.get(url)

if res:
    print('Response OK')
else:
    print('Response Failed')

# print(res.headers["Content-Type"])
# print(res.text)
print(res.text.find("Did you know"))
