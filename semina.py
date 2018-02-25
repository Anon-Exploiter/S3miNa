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

#####################################################################################################
        ################################   Importing Packages   ################################ 
#####################################################################################################

from insides import *
from sys 	 import argv
from core 	 import AnimeDownloader
import optparse
import socket
import httplib

print(Banner)

parser 	= optparse.OptionParser(
	usage=config._usage,
	version=config._version,
	conflict_handler="resolve"
)
general = optparse.OptionGroup(parser, c + 'General Options(Commands)')
general.add_option( '-h', '--help', 	action='help', 			dest='help', 	help='Shows help for S3miNa.')
general.add_option( '-V', '--version', 	action='version', 		dest='ver',	 	help='Shows version of S3miNa.')
general.add_option( '--url',			action='store', 		dest='url', 	help='URL of the Anime!')

info 	= optparse.OptionGroup(parser, w + "Arguments")
info.add_option( "-S", "--single",  	action='store_true',	dest='file',	help="For Downloading A Single Video")
info.add_option( "-s", "--subbed",  	action='store_true', 	dest='subbed', 	help="For Downloading Subbed Episode/Anime If Available")
info.add_option( "-d", "--dubbed",  	action='store_true', 	dest='dubbed', 	help="For Downloading Dubbed Episode/Anime If Available")
info.add_option( "--start",  			action='store', 		dest='start', 	help="For Starting From a Specific Video To End")
info.add_option( "--end",  				action='store', 		dest='end', 	help="For Ending to A Specific Video From Start")
info.add_option( "-h", "--hidden",  	action='store_true', 	dest='hidden', 	help="Pl0x Don't Use This Option")

grouped_scanning = optparse.OptionGroup(parser, g + "For Doing Everything At Once")
grouped_scanning.add_option( "-n", "--noshit",  action='store_true', dest='noshit', help="Just Enter The URL And Sit Back Tight and Enjoy!")

parser.add_option_group(general)
parser.add_option_group(info)
parser.add_option_group(grouped_scanning)

(options, args) = parser.parse_args()

if len(argv) == 1:
	parser.print_help()


try:

	if options.url:
		anime 	= options.url

	elif (not(options.url)):
		try: anime = args[0]
		except: pass

	try: _website = removeHTTP(website)
	except: pass

	try:
		if "/" in anime:
			_website = _website.split("/")[0]
			conn = httplib.HTTPConnection(_website)
			conn.connect()
	except (socket.gaierror, httplib.HTTPResponse):
		print w + "[" + g + "$" + w + "] " + r + "Sorry! " + g + str(_website) + c + " Seems To Be Offline || Your Internet's Not Working!"
		exit(Footer)

	if options.hidden:
		write(var="~", color=g, data="L0L: {}Nigga Why You Wasting My Time xD ?".format(c))

	elif options.noshit:
		AnimeDownloader(url=anime, subbed=False, dubbed=False, start=False, end=False, single=False)

	elif options.file:

		if options.subbed:
			AnimeDownloader(url=anime, subbed=True, dubbed=False, start=False, end=False, single={'_url': anime})

		elif options.dubbed:
			AnimeDownloader(url=anime, subbed=False, dubbed=True, start=False, end=False, single={'_url': anime})

		else:
			AnimeDownloader(url=anime, subbed=False, dubbed=False, start=False, end=False, single={'_url': anime})

	elif options.subbed:
		AnimeDownloader(url=anime, subbed=True, dubbed=False, start=False, end=False, single=False)

	elif options.dubbed:
		AnimeDownloader(url=anime, subbed=False, dubbed=True, start=False, end=False, single=False)

	elif options.start:
		options.start 	= 	int(options.start)
		AnimeDownloader(url=anime, subbed=False, dubbed=False, start={'count': options.start}, end=False, single=False)

	elif options.end:
		options.end 	= 	int(options.end)
		AnimeDownloader(url=anime, subbed=False, dubbed=False, start=False, end={'count': options.end}, single=False)

	# AnimeDownloader(url=anime, subbed=False, dubbed=False, start=False, end=False, single={'_url': 'http://www.animegg.org/bleach-episode-15#subbed'})

except NameError:
	pass

except KeyboardInterrupt:
    write(var="~", color=w, data="{}Err0r{}: {}User Interrupted!{}".format(r, w, g, " " * 15))
    
# except Exception, e:
#     write(var="#", color=r, data="Err0r: Kindly Report the err0r below to An0n3xPloiTeR :) (If Your Internet's Working ;)\n\"\"\"\n" + str(e) + "\n\"\"\"")

print(Footer)


















# from requests
# from bs4 import BeautifulSoup
# import re
# from os import system as execute
# from os import chdir, mkdir
# import os
# from time import sleep

# anime 	 = "bleach"
# language = "subbed"

# _headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Encoding': 'gzip,deflate,sdch',
#     'Accept-Language': 'en-US,en;q=0.8',
#     'Connection': 'close'
# }

# url 	= "http://www.animegg.org"

# lang 	= "#" + language

# combo 	= url + "/series/" + anime + lang
# lis 	= []

# request = requests.get(combo, headers=_headers).content
# soup 	= BeautifulSoup(request, 'lxml')
# res 	= soup.find_all('a', {'class': 'anm_det_pop'})
# for x in res:
# 	com = url + x['href']
# 	lis.append(com)

# lis = lis[:-139]
# lis = lis[::-1]

# try:
# 	for x in lis:

# 		website = "http://www.animegg.org"

# 		# The episode count!
# 		name	= "_".join(x.split("/")[3].split("#")[0].split("-")).capitalize()
# 		print("\n[$] Downloading: " + str(x) + "")

# 		request = requests.get(x, headers=_headers).content

# 		# Regex's for matching for some strings!
# 		reg1 	= r'<iframe src=\"(.*?)\" allowfullscreen style=\"border: 0; padding: 0; margin: 0; overflow: hidden;\" scrolling=\"no\" class=\"video\"><\/iframe>'
# 		reg2 	= r'\{file: \"(.*?)\",'
# 		title 	= r'<span class=\"e4tit\">(.*?)<\/span>'

# 		# the count of episode + the name of the file!
# 		title 	= str(re.findall(title, request)[0].replace(' ', '_').replace(':', '').replace('!', '').replace('?', '').replace('\'', '').replace('/', '').replace('.', '')) + ".mp4"
# 		combo 	= name + '-' + title
# 		combo 	= combo.replace(",", "")

# 		# print the title of the file to downloads
# 		print("[#] Title: " + str(combo) + "\n")

# 		# For finding the downloading link of that file!
# 		url1 	= website + str(re.findall(reg1, request)[1])
# 		request = requests.get(url1, headers=_headers).content

# 		# for reversing the regexed list because the last one is the highest resolution and then download it B)
# 		# url2 	= website + re.findall(reg2, request)[::-1][0]

# 		# for lower resolution! that's all we get :| 
# 		url2 	= website + re.findall(reg2, request)[0]
# 		print url2

# 		# For downloading the file `quitely`
		
# 		command = 'idman /d "' + str(url2) + '" /p C:\Users\umara\Desktop\\anime\ /f ' + str(combo) + ' /n'
# 		# command = 'idman /d "http://umarshah.tk/l0l.zip" /p C:\Users\umara\Desktop\\anime\ /f "l0l.zip" /n'
# 		# command = 'wget --show-progress --header="Referer: http://animegg.org" --output-document="' + str(combo) + '" ' + str(url2)
# 		print command
# 		execute(command)

# 		while not(os.path.isfile(combo)):
# 			sleep(0.1)
# 		else:
# 			continue

# except Exception, e:
# 	print("\n[#] Err0r: An Err0r Occured!\n[~] Kindly Report This Err0r To An0n 3xPloiTeR (if your internet's working :)\n\"\"\"" + str(e) + "\"\"\"")