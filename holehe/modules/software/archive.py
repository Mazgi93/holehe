from holehe.core import *
from holehe.localuseragent import *


def archive(email):
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------',
        'Origin': 'https://archive.org',
        'Connection': 'keep-alive',
        'Referer': 'https://archive.org/account/signup',
        'Sec-GPC': '1',
        'TE': 'Trailers',
    }

    data = '-----------------------------\r\nContent-Disposition: form-data; name="input_name"\r\n\r\nusername\r\n-----------------------------\r\nContent-Disposition: form-data; name="input_value"\r\n\r\n'+email+'\r\n-----------------------------\r\nContent-Disposition: form-data; name="input_validator"\r\n\r\ntrue\r\n-----------------------------\r\nContent-Disposition: form-data; name="submit_by_js"\r\n\r\ntrue\r\n-------------------------------\r\n'

    response = requests.post('https://archive.org/account/signup', headers=headers, data=data)
    if "is already taken." in response.text:
        return({"rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": None})
    else:
        return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
