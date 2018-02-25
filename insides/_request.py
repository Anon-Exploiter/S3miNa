"""
_______________.___.
\______   \__  |   |
 |    |  _//   |   |
 |    |   \\____   |
 |______  // ______|
        \/ \/       
   _____         _______           ________        __________.__         ._____________   __________ 
  /  _  \   ____ \   _  \   ____   \_____  \___  __\______   |  |   ____ |__\__    _______\______   \
 /  /_\  \ /    \/  /_\  \ /    \    _(__  <\  \/  /|     ___|  |  /  _ \|  | |    |_/ __ \|       _/
/    |    |   |  \  \_/   |   |  \  /       \>    < |    |   |  |_(  <_> |  | |    |\  ___/|    |   \
\____|__  |___|  /\_____  |___|  / /______  /__/\_ \|____|   |____/\____/|__| |____| \___  |____|_  /
        \/     \/       \/     \/         \/      \/                                     \/       \/ 

                                ~ Changing Coder Name Wont Make You One :)
                                             ~ An0n 3xPloiTeR :)
"""

import requests

_headers = {
    'User-Agent'        : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept'            : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding'   : 'gzip,deflate,sdch',
    'Accept-Language'   : 'en-US,en;q=0.8',
    'Connection'        : 'close',
}

def Request(website, _timeout=5, __resp_code=False, __req_body=False, _post=False, __post_data=False, _redir=False):
    try:
        if __req_body == False:
            if _post == False:
                if __resp_code == False:
                    request = requests.get(website, timeout=_timeout, headers=_headers, allow_redirects=_redir).text.encode('UTF-8')
                    return(request)
                elif __resp_code == True:
                    request = requests.get(website, timeout=_timeout, headers=_headers, allow_redirects=_redir).status_code
                    return(request)

            if _post == True:
                if __resp_code == False:
                    request = requests.post(website, timeout=_timeout, headers=_headers, allow_redirects=_redir, data=__post_data).text.encode('UTF-8')
                    return(request)
                elif __resp_code == True:
                    request = requests.post(website, timeout=_timeout, headers=_headers, allow_redirects=_redir, data=__post_data).status_code
                    return(request)

        elif __req_body == True:
            if _post == False:
                request = requests.get(website, timeout=_timeout, headers=_headers, allow_redirects=_redir)
                return(request)

            if _post == True:
                request = requests.post(website, timeout=_timeout, headers=_headers, allow_redirects=_redir, data=__post_data)
                return(request)
    except requests.exceptions.ConnectionError:
        pass

    except requests.exceptions.ReadTimeout:
        pass