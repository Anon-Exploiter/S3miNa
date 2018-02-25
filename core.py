from insides import *
from bs4 	 import BeautifulSoup
from re 	 import findall
from sys 	 import stdout
from time 	 import time
import os

def AnimeDownloader(url, subbed=True, dubbed=False, start=False, end=False, single=False, quality=False):

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
		try:
			request 	= Request(url, _timeout=5, _redir=True, __req_body=True)
			request 	= request.text.encode('utf-8')
			return(request)
		except AttributeError:
			try:
				write("{}!".format(r), c, data="{:<15}{}~> {}Your Internet Speed Seems Slow {} ".format("Warning", w, r, ":{"))
				request 	= Request(url, _timeout=5, _redir=True, __req_body=True)
				request 	= request.text.encode('utf-8')
				return(request)
			except AttributeError:
				print("sd")


	def parse(data):
		soup 		= BeautifulSoup(data, 'lxml')
		_list 		= soup.find_all('a', class_="anm_det_pop")
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

			# if subbed == True:
			# 	combination 	= website + links['href'] + "#subbed"

			# elif dubbed == True:
			# 	combination 	= website + links['href'] + "#dubbed"

			# else:
			# 	combination 	= website + links['href'] + "#subbed"

			_lis.append(combination)
			# print(links)
		return(_lis)

	def download(_list, __name):

		if single == False:
			for links in _list:
				# print links
				write("~", c, data="{:<15}{}~> {}{}".format("Downloading", w, g, links))
				request		= _request(links)
				# print request
				__links_reg = r'<iframe src=\"(.*?)\" allowfullscreen style=\"border: 0; padding: 0; margin: 0; overflow: hidden;\" scrolling=\"no\" class=\"video\"><\/iframe>'
				__name_reg 	= r'<span class=\"e4tit\">(.*?)<\/span>'
				_links 		= findall(__links_reg, request)
				__vid_name 	= findall(__name_reg, request)[0]
				__vid_name 	= (__vid_name.replace("amp;", "").replace("amp", "").replace("&", "").replace("&amp;", "").replace(",", "").replace(")", "").replace("(", "").replace("]", "").replace("[", "").replace("#", "").replace(' ', '_').replace(':', '').replace('!', '').replace('?', '').replace('\'', '').replace('/', '').replace('.', '') + ".mp4").capitalize()
				write("~", g, data="{:<15}{}~> {}{}".format("Title", w, c, __vid_name.replace(".mp4", "")))


				if len(_links) <= 5:
					# Downloads Subbed / Dubbed
					if subbed == True:
						link 	= _links[0]

					elif dubbed == True:
						link 	= _links[1]

					else:
						link 	= _links[0]

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
					__file_name = (removeHTTP(links).replace("www.", "").replace("animegg.org", "").replace("/", "").replace("-", "_") + "_" + __vid_name).capitalize()
					command 	= 'idman /d "' + str(combination) + '" /p ' + anime_path + '/ /f ' + str(__file_name) + ' /n'
					# print command
					os.system(command)
					
					while not(os.path.isfile(anime_path + "/" + __file_name)):
						stdout.write("\r{}[{}!{}]{} {:<15}{}~> {}Downloading ...\r".format(w, y, w, c, "Status", w, y))
						sleep(0.1)
					
					else:
						sleep(0.1)
						stdout.write("{}[{}#{}]{} {:<15}{}~> {}Completed{}\n\n".format(w, g, w, c, "Status", w, g, " " * 10))
						continue
					t2 			= time()
					total 		= (t2 - t1 - 0.1)
					total 		= str(total)
					total 		= total[:4]
					write("*", g, data="{:<15}{}~> {}{} seconds...\n".format("Total Time", w, c, total))


		else:
			t1 			= time()
			__url 		= single['_url']
			url_		= __url.replace("#", "").replace("subbed", "").replace("raw", "").replace("dubbed", "")
			write("~", c, data="{:<15}{}~> {}{}".format("Downloading", w, g, url_))
			request		= _request(__url)
			# print request
			__links_reg = r'<iframe src=\"(.*?)\" allowfullscreen style=\"border: 0; padding: 0; margin: 0; overflow: hidden;\" scrolling=\"no\" class=\"video\"><\/iframe>'
			__name_reg 	= r'<span class=\"e4tit\">(.*?)<\/span>'
			_links 		= findall(__links_reg, request)
			__vid_name 	= findall(__name_reg, request)[0]
			__vid_name 	= (__vid_name.replace(' ', '_').replace(':', '').replace('!', '').replace('?', '').replace('\'', '').replace('/', '').replace('.', '') + ".mp4").capitalize()
			write("~", g, data="{:<15}{}~> {}{}".format("Title", w, c, __vid_name.replace(".mp4", "")))

			if len(_links) <= 5:
				if subbed == True:
					link 	= _links[0]

				elif dubbed == True:
					link 	= _links[1]

				else:
					link 	= _links[0]

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
				__file_name = (removeHTTP(__url).replace("#", "").replace("subbed", "").replace("dubbed", "").replace("raw", "").replace("www.", "").replace("animegg.org", "").replace("/", "").replace("-", "_") + "_" + __vid_name).capitalize()
				command 	= 'idman /d "' + str(combination) + '" /p ' + anime_path + '/ /f ' + str(__file_name) + ' /n'
				# print command
				os.system(command)

				# print anime_path
				# print __file_name
				
				while not(os.path.isfile(anime_path + "/" + __file_name)):
					stdout.write("\r{}[{}!{}]{} {:<15}{}~> {}Downloading ...\r".format(w, y, w, c, "Status", w, y))
					sleep(0.1)
				
				else:
					sleep(0.1)
					stdout.write("{}[{}#{}]{} {:<15}{}~> {}Completed{}\n".format(w, g, w, c, "Status", w, g, " " * 10))

				t2 			= time()
				total 		= (t2 - t1 - 0.1)
				total 		= str(total)
				total 		= total[:4]
				write("*", g, data="{:<15}{}~> {}{} seconds...".format("Total Time", w, c, total))

	url 	= _new(url)
	_url	= removeHTTP(_new(url))
	heading("Downloading", header(_url), g, afterWebHead="")
	data 	= _request(url)
	_list 	= parse(data)
	# print _list
	download(_list, __name=header(_url, forSingle=True))