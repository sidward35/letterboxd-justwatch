from pprint import pprint
import urllib.request
import ssl
from bs4 import BeautifulSoup
from justwatch import JustWatch

just_watch = JustWatch(country='US')
services = ['amp', 'nfx', 'stv', 'hmf', 'pct', 'pcp', 'fmn', 'rkc', 'yfr', 'tcw', 'cws', 'vuf', 'pbs', 'tbv', 'knp', 'com', 'cru', 'abc', 'crk', 'his', 'aae', 'lft', 'pcf', 'bmg', 'dvc', 'ytv', 'mot', 'lol', 'ssc', 'ptv', 'vix', 'sft', 'tfd', 'vtv', 'ctw', 'ads', 'usn', 'vik', 'dkm', 'brv', 'fnw', 'ind', 'ahc', 'tlc', 'hgt', 'diy', 'inv', 'sci', 'dea', 'apl', 'dil', 'dis', 'coo', 'tra', 'hrv', 'ltv', 'vho', 'flr', 'rvy', 'rst', 'hyh', 'vrv', 'dpu', 'plx', 'own', 'fmz', 'bph', 'hoc', 'aim', 'pdm'] # set streaming services to search (in order)
letterboxd_username = 'sidward35'
watchlist_pages = 4

# get watchlist
watchlist_titles = []
#watchlist_years = []

ssl._create_default_https_context = ssl._create_unverified_context
html_str = ''
for i in range(watchlist_pages):
	fp = urllib.request.urlopen("https://letterboxd.com/"+letterboxd_username+"/watchlist/by/popular/page/"+str(i+1))
	html_str+=fp.read().decode("utf8")
	fp.close()

soup = BeautifulSoup(html_str, 'html.parser')
html_objects = soup.findAll('li', {'class': 'poster-container'})
for html_object in html_objects:
	object_str = str(html_object).replace('&amp;','&')
	start_index = object_str.index('<img alt="')+10
	end_index = object_str.index('"', start_index)
	movie_name = object_str[start_index:end_index]
	watchlist_titles.append(movie_name)
print(watchlist_titles)


result = {}
for service in services:
	service_list = []
	indexes_to_remove = []
	for i in range(len(watchlist_titles)):
		movie = watchlist_titles[i]
		#year = watchlist_years[i]
		#movies_found = just_watch.search_for_item(query=movie+' '+year, providers=[service], monetization_types=['flatrate'])
		if service=='amp' or service=='nfx' or service=='stv': # for paid services
			movies_found = just_watch.search_for_item(query=movie, providers=[service], monetization_types=['flatrate', 'free', 'ads'])
		else: # for free services
			movies_found = just_watch.search_for_item(query=movie, providers=[service], monetization_types=['free', 'ads'])
		if len(movies_found['items'])>0 and movies_found['items'][0]['title'] == movie:
			service_list.append(movie+' ('+str(movies_found['items'][0]['original_release_year'])+')') 
			indexes_to_remove.append(i)
	for i in sorted(indexes_to_remove, reverse=True):
		watchlist_titles.pop(i) # remove movie from overall watchlist
		#watchlist_years.pop(i)

	result[service] = service_list

# remaining movies in watchlist ==> other
other_list = []
for i in range(len(watchlist_titles)):
	#other_list.append(watchlist_titles[i]+' ('+watchlist_years[i]+')')
	other_list.append(watchlist_titles[i])
result['other'] = other_list

pprint(result)
