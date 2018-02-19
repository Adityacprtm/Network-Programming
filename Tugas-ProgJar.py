import http.client
import json

def get(domain, url):
    conn = http.client.HTTPSConnection(domain)
    conn.request("GET", url)
    response = conn.getresponse()
    x = response.read()
    return json.loads(x)

isbn = input('masukan isbn : ')
data = get("www.googleapis.com", "/books/v1/volumes?q="+isbn)
print("Judul: " + data['items'][0]['volumeInfo']['title'])
print("Pengarang: ")
for nama in data['items'][0]['volumeInfo']['authors']:
    print(" - " + nama)
print("Penerbit: " + data['items'][0]['volumeInfo']['publisher'])
print("Tanggal terbit: " + data['items'][0]['volumeInfo']['publishedDate'])