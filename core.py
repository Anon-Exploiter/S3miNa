from insides import *
from bs4 	 import BeautifulSoup
from re 	 import findall
from sys 	 import stdout
import os

def AnimeDownloader(url, subbed=False, dubbed=False, start=False, end=False, single=False, quality=False):

	def _new(url):
		"""
		Generates A new And Clean Url
		"""
		if "/" in url[::-1][0]:
			url 	= "/".join(url.split("/")[:-1])
			return(addHTTP(url))
		return(addHTTP(url))

	def header(url, forSingle=False):
		"""
		Displays a Small Header Along With The Name of The Anime!
		"""
		url 	= url.split("/")
		name 	= url[::-1][0]
		_name 	= []
		if "-" in name:
			name 	= name.split("-")
			if forSingle == True:
				return("-".join(name).capitalize())
			for name in name:
				_name.append(name.capitalize())
			name 	= "-".join(_name)
			name 	= name.replace("#", "").replace("subbed", "").replace("dubbed", "")
			return(name)
		else:
			name 	= name.replace("#", "").replace("subbed", "").replace("dubbed", "")
			return(name.capitalize())

	def _request(url):
		"""
		Makes A Nice And Botiphul Request :} 
		"""
		try:
			request 	= Request(url, _timeout=5, _redir=True, __req_body=True).text
			return(request)
		except AttributeError:
			try:
				write("{}!".format(r), c, data="{:<15}{}~> {}Your Internet Speed Seems Slow {}".format("Warning", w, r, ":{"))
				request 	= Request(url, _timeout=5, _redir=True, __req_body=True)
				request 	= request.text.encode('utf-8')
				return(request)
			except AttributeError:
				write("{}!".format(r), c, data="{}{:<15}{}~> {}You Better Get Some Bandwidth NiGGa {}".format(g, "S3d-N0t3", w, r, ":')"))
				exit(Footer)


	def parse(data):
		"""
		Parses The Data and Return List Of Links Of Episodes To Download
		"""
		soup 		= BeautifulSoup(data, 'lxml')
		_list 		= soup.find_all('a', class_="anm_det_pop")

		# print(str(end['count']))

		if start != False:
			_count 		= start['count']
			_count 		= _count - 1
			_list 		= _list[:-_count]
			_list 		= _list[::-1]

		elif end != False:
			_count 		= end['count']
			_list 		= _list[::-1]
			_list 		= _list[:_count]

		else:
			_list 		= _list[::-1]

		_lis 		= []
		for links in _list:

			combination 	= website + links['href']

			_lis.append(combination)
		return(_lis)

	def filter(_links):
		"""
		An Alternate To Finding Subbed / Dubbed Episodes :')
		Lots Of Bullshit :p 
		"""

		if len(_links) == 3:
			if subbed == True:
				link 	= _links[1]

			elif dubbed == True:
				link 	= _links[2]

			else:
				link 	= _links[1]

		elif len(_links) == 2:
			if subbed == True:
				link 	= _links[0]

			elif dubbed == True:
				link 	= _links[1]

			else:
				link 	= _links[0]


		elif len(_links) == 1:
			if dubbed == True:
				write("{}!".format(r), c, data="{}{:<15}{}~> {}Dubbed Not Available; {}Downloading Subbed! {}".format(r, "Inf0", w, c, g, w+":{"))
				link 		= _links[0]
			else:
				link 		= _links[0]

		elif len(_links) == 0:
			write("{}!".format(r), c, data="{}{:<15}{}~> {}Bruh! It seems this episode isn't up yet {}".format(r, "D@mN", w, g, w+":')"))

		else:
			print(len(_links))
			print(_links)
			link 			= _links[0]

		return(link)

	def download(_list, __name):
		"""
		Downloads The Episode / Episodes
		Requires Lots Of Man Power XD
		"""

		referer = "https://animegg.org/embed/12345"
		if single == False:
			for links in _list:

				write("~", c, data="{:<15}{}~> {}{}".format("Downloading", w, g, links))
				request		= _request(links)

				__links_reg = r'<iframe src=\"(.*?)\" allowfullscreen style=\"border: 0; padding: 0; margin: 0; overflow: hidden;\" scrolling=\"no\" class=\"video\"><\/iframe>'
				__name_reg 	= r'<span class=\"e4tit\">(.*?)<\/span>'

				_links 		= findall(__links_reg, request)
				__vid_name 	= findall(__name_reg, request)[0]
				__vid_name 	= (__vid_name.replace("amp;", "").replace("amp", "").replace("&", "").replace("&amp;", "").replace(",", "").replace(")", "").replace("(", "").replace("]", "").replace("[", "").replace("#", "").replace(' ', '_').replace(':', '').replace('!', '').replace('?', '').replace('\'', '').replace('/', '').replace('.', '') + ".mp4").capitalize()
				write("~", g, data="{:<15}{}~> {}{}".format("Title", w, c, __vid_name.replace(".mp4", "")))

				link = filter(_links)

				combination = website + link
				request 	= _request(combination)

				__file_reg 	= r'\{file: \"(.*?)\",'
				file_link 	= findall(__file_reg, request)[0]

				path 	 	= os.getcwd() + "/"
				anime_dir 	= os.getcwd() + "/" + "animes"
				anime_path 	= os.getcwd() + "/" + "animes" + "/" + __name


				if not(os.path.isdir(anime_dir)):
					os.mkdir(anime_dir)
					if not(os.path.isdir(anime_path)):
						os.mkdir(anime_path)

				combination = website + file_link
				__file_name = (removeHTTP(links).replace("www.", "").replace("animegg.org", "").replace("/", "").replace("-", "_") + "_" + __vid_name).capitalize().replace("`", "")

				### Use whatever program you want to download (uncomment the one you want, comment the one you don't :)
				# command 	= 'idman /d "' + str(combination) + '" /p "' + anime_path + '/" /f ' + str(__file_name) + ' /n'
				command         = "axel --num-connections=16 -a --header=\"Referer: " + referer + "\" --output=\"" + anime_path + "/" + __file_name + "\" " + combination
				os.system(command)

				while not(os.path.isfile(anime_path + "/" + __file_name)):
					stdout.write("\r{}[{}!{}]{} {:<15}{}~> {}Downloading ...\r".format(w, y, w, c, "Status", w, y))
					sleep(0.1)

				else:
					sleep(0.1)
					stdout.write("{}[{}#{}]{} {:<15}{}~> {}Completed{}\n\n".format(w, g, w, c, "Status", w, g, " " * 10))
					continue

		else:
			__url 		= single['_url']
			url_		= __url.replace("#", "").replace("subbed", "").replace("raw", "").replace("dubbed", "")

			write("~", c, data="{:<15}{}~> {}{}".format("Downloading", w, g, url_))
			request		= _request(__url)

			__links_reg = r'<iframe src=\"(.*?)\" allowfullscreen style=\"border: 0; padding: 0; margin: 0; overflow: hidden;\" scrolling=\"no\" class=\"video\"><\/iframe>'
			__name_reg 	= r'<span class=\"e4tit\">(.*?)<\/span>'

			_links 		= findall(__links_reg, request)
			__vid_name 	= findall(__name_reg, request)[0]
			__vid_name 	= (__vid_name.replace(' ', '_').replace(':', '').replace('!', '').replace('?', '').replace('\'', '').replace('/', '').replace('.', '') + ".mp4").capitalize()

			write("~", g, data="{:<15}{}~> {}{}".format("Title", w, c, __vid_name.replace(".mp4", "")))

			link = filter(_links)

			combination = website + link
			request 	= _request(combination)
			__file_reg 	= r'\{file: \"(.*?)\",'
			file_link 	= findall(__file_reg, request)[0]

			path 	 	= os.getcwd() + "/"
			anime_dir 	= os.getcwd() + "/" + "animes"
			anime_path 	= os.getcwd() + "/" + "animes" + "/" + "Single_Episodes"


			if not(os.path.isdir(anime_dir)):
				os.mkdir(anime_dir)
				if not(os.path.isdir(anime_path)):
					os.mkdir(anime_path)

			combination = website + file_link
			__file_name = (removeHTTP(__url).replace("#", "").replace("subbed", "").replace("dubbed", "").replace("raw", "").replace("www.", "").replace("animegg.org", "").replace("/", "").replace("-", "_") + "_" + __vid_name).capitalize()
			### Use whatever program you want to download (uncomment the one you want, comment the one you don't :)
			#command 	= 'idman /d "' + str(combination) + '" /p "' + anime_path + '/" /f ' + str(__file_name) + ' /n'
			command         = "axel --num-connections=10 -a --header=\"Referer: " + referer + "\" --output=\"" + anime_path + "/" + __file_name + "\" " + combination
			print(command)
			os.system(command)

			while not(os.path.isfile(anime_path + "/" + __file_name)):
				stdout.write("\r{}[{}!{}]{} {:<15}{}~> {}Downloading ...\r".format(w, y, w, c, "Status", w, y))
				sleep(0.1)
			else:
				sleep(0.1)
				stdout.write("{}[{}#{}]{} {:<15}{}~> {}Completed{}\n".format(w, g, w, c, "Status", w, g, " " * 10))


	heading("Downloading", header(removeHTTP(_new(url))), g, afterWebHead="")
	download(parse(_request(_new(url))), __name=header(removeHTTP(_new(url)), forSingle=True))
