import requests

bright_red = "\033[0;91m"

domain = input("Enter Domain Name: ")
file = open("url.txt")
content = file.read()
subdomains = content.splitlines()
for subdomain in subdomains:
    url = f"http://{domain}.{subdomain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print(bright_red+"[+]Discovered subdomain:",url)