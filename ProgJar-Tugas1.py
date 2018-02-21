import http.client
import json

judul = ""
pengarang = ""
penerbit = ""
thn = ""

def get(domain, url):
    conn = http.client.HTTPSConnection(domain)
    conn.request("GET", url)
    response = conn.getresponse()
    a = response.read()
    return json.loads(a)

def set(data): 
    global judul
    judul = data['items'][0]['volumeInfo']['title']
    global pengarang
    pengarang = data['items'][0]['volumeInfo']['authors']
    global penerbit
    penerbit = data['items'][0]['volumeInfo']['publisher']
    global thn
    thn = data['items'][0]['volumeInfo']['publishedDate']

def show():
    print("Judul = " + judul)
    print("Pengarang = ")
    for i in pengarang:
        print("- "+i)
    print("Penerbit = " + penerbit)
    print("Tanggal terbit = " + thn)

isbn = input('masukan isbn : ')
#Jika ada eror, hapus keynya
data = get("www.googleapis.com", "/books/v1/volumes?q=isbn:"+isbn+"&key=AIzaSyC2oAuT04JNRVZOp86BbeQi6JT-J4-HLvs")
set(data)
show()