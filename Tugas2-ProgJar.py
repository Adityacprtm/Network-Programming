import http.client
import json

def get(domain, url):
    conn = http.client.HTTPSConnection(domain)
    conn.request("GET", url)
    response = conn.getresponse()
    a = response.read()
    return json.loads(a)

nama = input('masukan pengarang : ')
data = get("www.googleapis.com", "/books/v1/volumes?q="+nama)
print("Pengarang: " + data['items'][0]['volumeInfo']['authors'])
print("judul: ")
for judul in data['items'][0]['volumeInfo']['title']:
    print(" - " + judul)