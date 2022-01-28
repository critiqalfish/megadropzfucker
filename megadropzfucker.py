import requests
import timeit
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

class Error(Exception):
    pass

class InvalidLinkError(Error):
    def __init__(self):
        pass
    def __str__(self):
        return ("InvalidLinkError")

class BypassError(Error):
    def __init__(self):
        pass
    def __str__(self):
        return ("BypassError")

class RequestError(Error):
    def __init__(self):
        pass
    def __str__(self):
        return ("RequestError")

class LinkNotFoundError(Error):
    def __init__(self):
        pass
    def __str__(self):
        return ("LinkNotFoundError")

class OtherError(Error):
    def __init__(self):
        pass
    def __str__(self):
        return ("OtherError")

def link(link0, proxy=False):
    try: bypassed_link = requests.get(f'https://bypass.bot.nu/bypass2?url={link0}').json()
    except: raise RequestError()
    if not 'msg' in bypassed_link and bypassed_link['success']: pass
    elif not bypassed_link['success']: raise InvalidLinkError()
    print(bypassed_link['destination'])
    if proxy:
        try: scraped_pastebin = requests.get(bypassed_link['destination'], proxies={'http': config['KEYS']['proxykey'], 'https': config['KEYS']['proxykey']}).text
        except: raise RequestError()
    elif not proxy:
        try: scraped_pastebin = requests.get(f"http://api.scraperapi.com?api_key={config['KEYS']['apikey']}&url={bypassed_link['destination']}").text
        except: raise RequestError()
    try: extracted_link = scraped_pastebin[scraped_pastebin.index('<textarea class="textarea">')+len('<textarea class="textarea">'):scraped_pastebin.index('</textarea>')]
    except: raise LinkNotFoundError()
    try:
        if extracted_link.startswith('STEP 2:'):
            u = link(extracted_link.removeprefix('STEP 2: '))
            f = []
            for x in u:
                if x == '\r': pass
                else:
                    y = x.replace(' \r', '')
                    z = y.replace('\r', '')
                    f.append(z)
            return ' '.join(f).split()
        else:
            return extracted_link.split('\n')
    except: raise OtherError()

if __name__ == '__main__':
    print('[AVERAGE]: ', 0.1 * int(timeit.timeit(lambda: print(link('https://link-center.net/156589/87347845', False)), number=10)))