from colors import *
from time   import sleep
import requests
import re

_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

empty_Website = "\n\t{red}[=] Please Enter A Website :/\n\t\t{cyan}~ An0n 3xPloiTeR :)".format(red=r, cyan=c)

wrong_URL = "\n\t{red}[=] Please Enter a Valid And Correct URL (i.e, hackthissite.org, hack.me)\n\t\t{cyan}~ An0n 3xPloiTeR :)".format(red=r, cyan=c)

str_Index = "\n\t{red}[=] Please Input a Integer (i.e, 1, 2, 3) :\\\n\t\t{cyan}~ An0n 3xPloiTeR :)".format(red=r, cyan=c)

val_Select = "\t{}[$] Please Use The Index Value From The List\n\t\t[+] Not By Your Own :/\n\t\t\t ~ An0n 3xPloiTeR  \n".format(r)

def webNotEmpty(website):
    """
    Check Whether if the website is empty or not and return valid / !valid
    """
    if len(website) >= 1:
        return "valid"
    else:
        return "!valid"

def validWebsite(website):
    """
    Checks With a Regex If The URL Entered Is Correct Or Not! (User can use IP Too :)
    """
    # web = webNotEmpty(website)
    # if web is "valid":
    #     if not (re.match(r"(^(http://|https://)?([a-z0-9][a-z0-9-]*\.)+[a-z0-9][a-z0-9-]*$)", website)):
    #         exit(wrong_URL)
    # else:
    #     exit(empty_Website)
    return(website)

def cleanURL(website):
    """
    Removes ["http://", "http://www.", "https://", "https://www.", "www."] from the start of the Url!
    """
    web = validWebsite(website)
    website = website.replace("http://", "")
    website = website.replace("http://www.", "")
    website = website.replace("https://", "")
    website = website.replace("https://www.", "")
    # website = website.replace("www.", ""); 
    return(website)

def removeHTTP(website):
    """
    Removes ["http://", "http://www.", "https://", "https://www.", "www."] from the start of the Url and returns it!
    """
    website = cleanURL(website); return(website)

def addHTTP(website):
    """
    Removes ["http://", "http://www.", "https://", "https://www.", "www."] from the start of the Url and add a "http://" in the start again and return it!
    """
    website = cleanURL(website)
    website = ("http://" + website); return(website)

def _stop(time):
    sleep(int(time))

def write(var, color, data):
    if var == None:
        print(color + str(data))
    elif var != None:
        print(w + "[" + g + var + w + "] " + color + str(data))

def _heading(heading, c, var):
    name    = var
    # name    = u'\u2500'
    space   = " " * 7
    var     = str(space + heading + " ..." + space)
    length  = len(var) + 1; print "" # \n
    print("{white}" + name * length + name).format(white=w)
    print("{color}" + var).format(color=c)
    print("{white}" + name * length + name).format(white=w); print "" # \n

def heading(heading, website, color, afterWebHead):
    space = " " * 15
    webs = removeHTTP(website)
    if "/" in webs:
        webs = website.split("/")
        website = webs[0]

    var = str(space + heading + " '" + website + "'" + str(afterWebHead) + " ..." + space)
    length = len(var) + 1; print "" # \n
    print("{white}" + "-" * length + "-").format(white=w)
    print("{color}" + var).format(color=color)
    print("{white}" + "-" * length + "-").format(white=w); print "" # \n