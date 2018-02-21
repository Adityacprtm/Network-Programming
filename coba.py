import http.client


def get(domain, url):
    conn = http.client.HTTPSConnection(domain)
    conn.request("GET", url)
    response = conn.getresponse()
    return response.getheaders(), response.read()


for data in get("www.googleapis.com", "/books/v1/volumes?q=9781430230045"):
    print(data)
