import requests
"""
This file contains the 'setCookieRequest' function to set the 
required 'session cookie' for accessing a website.
Function 'scrapeRequest' conducts a get request to a website in
order to access html content.
"""

def setCookieRequest(url):
    resp = requests.get(url,
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','accept-encoding': 'gzip, deflate, br','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','upgrade-insecure-requests':'1'})
    cookies_dict = resp.cookies
    return cookies_dict

def scrapeRequest(url, cookies_dict):
    r = requests.get(url,cookies = cookies_dict,
                    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-language': 'en-US,en;q=0.9',
                            'upgrade-insecure-requests': '1',
                            'sec-fetch-dest' : 'document',
                            'sec-fetch-mode' : 'navigate',
                            'sec-fetch-site': 'none'})
    return r



