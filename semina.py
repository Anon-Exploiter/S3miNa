#!/usr/bin/python

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
		AnimeDownloader(url=anime, subbed=True, dubbed=False, start=False, end=False, single=False)

	elif options.file:

		if options.subbed:
			AnimeDownloader(url=anime, subbed=True, dubbed=False, start=False, end=False, single={'_url': anime})

		elif options.dubbed:
			AnimeDownloader(url=anime, subbed=False, dubbed=True, start=False, end=False, single={'_url': anime})

		else:
			AnimeDownloader(url=anime, subbed=True, dubbed=False, start=False, end=False, single={'_url': anime})

	elif options.subbed and not(options.start or options.end):
		AnimeDownloader(url=anime, subbed=True, dubbed=False, start=False, end=False, single=False)

	elif options.dubbed and not(options.start or options.end):
		AnimeDownloader(url=anime, subbed=False, dubbed=True, start=False, end=False, single=False)

	elif options.start:
		options.start 	= 	int(options.start)

		if options.subbed:
			AnimeDownloader(url=anime, subbed=True, dubbed=False, start={'count': options.start}, end=False, single=False)

		elif options.dubbed:
			AnimeDownloader(url=anime, subbed=False, dubbed=True, start={'count': options.start}, end=False, single=False)

		else:
			AnimeDownloader(url=anime, subbed=True, dubbed=False, start={'count': options.start}, end=False, single=False)

	elif options.end:
		options.end 	= 	int(options.end)

		if options.subbed:
			AnimeDownloader(url=anime, subbed=True, dubbed=False, start=False, end={'count': options.end}, single=False)

		elif options.dubbed:
			AnimeDownloader(url=anime, subbed=False, dubbed=True, start=False, end={'count': options.end}, single=False)

		else:
			AnimeDownloader(url=anime, subbed=True, dubbed=False, start=False, end={'count': options.end}, single=False)

	else:
		AnimeDownloader(url=anime, subbed=True, dubbed=False, start=False, end=False, single=False)

except NameError, e:
	if "anime" in str(e):
		pass

except KeyboardInterrupt:
    write(var="~", color=w, data="{}Err0r{}: {}User Interrupted!{}".format(r, w, g, " " * 15))

print(Footer)

# ~ See Ya :D
# ~ An0n 3xPloiTeR :)
