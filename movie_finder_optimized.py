from pprint import pprint
import urllib.request
import ssl
from bs4 import BeautifulSoup
from justwatch import JustWatch


service_codes = {'nfx': 'Netflix', 'amp': 'Amazon Prime Video', 'dnp': 'Disney Plus', 'atp': 'Apple TV Plus', 'itu': 'Apple iTunes', 'fuv': 'fuboTV', 'hlu': 'Hulu', 'hbm': 'HBO Max', 'hmf': 'HBO Max Free', 'pct': 'Peacock', 'pcp': 'Peacock Premium', 'amz': 'Amazon Video', 'ply': 'Google Play Movies', 'yot': 'YouTube', 'pmp': 'Paramount Plus', 'fmn': 'Funimation Now', 'ast': 'Starz Play Amazon Channel', 'app': 'Paramount+ Amazon Channel', 'aep': 'EPIX Amazon Channel', 'adp': 'Discovery+ Amazon Channel', 'ahb': 'HBO Now Amazon Channel', 'ash': 'Showtime Amazon Channel', 'azp': 'AMC Plus', 'hbn': 'HBO Now', 'rkc': 'The Roku Channel', 'srk': 'Showtime Roku Premium Channel', 'prk': 'Paramount+ Roku Premium Channel', 'sru': 'Starz Roku Premium Channel', 'ark': 'AMC+ Roku Premium Channel', 'erk': 'Epix Roku Premium Channel', 'koc': 'Kocowa', 'ytr': 'YouTube Premium', 'yfr': 'YouTube Free', 'hop': 'Hoopla', 'tcw': 'The CW', 'cws': 'CW Seed', 'vdu': 'Vudu', 'vuf': 'VUDU Free', 'stz': 'Starz', 'crc': 'Criterion Channel', 'sho': 'Showtime', 'pbs': 'PBS', 'pfx': 'Pantaflix', 'fxn': 'FXNow', 'tbv': 'Tubi TV', 'knp': 'Kanopy', 'com': 'Comedy Central', 'msf': 'Microsoft Store', 'cru': 'Crunchyroll', 'rbx': 'Redbox', 'snx': 'Sun Nxt', 'mxg': 'Max Go', 'abc': 'ABC', 'drv': 'DIRECTV', 'crk': 'Crackle', 'amt': 'AMC Theatres', 'amc': 'AMC', 'fnd': 'Fandor', 'cts': 'Curiosity Stream', 'nbc': 'NBC', 'epx': 'Epix', 'ffm': 'Freeform', 'his': 'History', 'sfy': 'Syfy', 'aae': 'A&E', 'lft': 'Lifetime', 'shd': 'Shudder', 'scb': 'Screambox', 'act': 'Acorn TV', 'sdn': 'Sundance Now', 'pcf': 'Popcornflix', 'gdc': 'GuideDoc', 'bbo': 'BritBox', 'rlz': 'realeyz', 'mbi': 'Mubi', 'nfk': 'Netflix Kids', 'pty': 'Pantaya', 'bmg': 'Boomerang', 'umc': 'Urban Movie Channel', 'hvt': 'History Vault', 'dvc': 'Dove Channel', 'ytv': 'Yupp TV', 'ern': 'Eros Now', 'mns': 'Magnolia Selects', 'wwe': 'WWE Network', 'mot': 'MyOutdoorTV', 'anh': 'Nickhits Amazon Channel', 'ang': 'Noggin Amazon Channel', 'htv': 'Hopster TV', 'lol': 'Laugh Out Loud', 'ssc': 'Smithsonian Channel', 'pux': 'Pure Flix', 'hmm': 'Hallmark Movies', 'lmc': 'Lifetime Movie Club', 'apk': 'PBS Kids Amazon Channel', 'abo': 'Boomerang Amazon Channel', 'acn': 'Cinemax Amazon Channel', 'apa': 'Pantaya Amazon Channel', 'ahm': 'Hallmark Movies Now Amazon Channel', 'apm': 'PBS Masterpiece Amazon Channel', 'avt': 'Viewster Amazon Channel', 'ame': 'MZ Choice Amazon Channel', 'sfx': 'Spamflix', 'stv': 'Sling TV', 'ptv': 'Pluto TV', 'hdv': 'HiDive', 'vix': 'VIX ', 'nfp': 'Night Flight Plus', 'tpc': 'Topic', 'mtv': 'MTV', 'rtc': 'Retrocrush', 'cla': 'Classix', 'dkk': 'Dekkoo', 'sft': 'Shout! Factory TV', 'chf': 'Chai Flicks', 'ovi': 'OVID', 'mhz': 'Mhz Choice', 'tfd': 'The Film Detective', 'vtv': 'Vice TV ', 'asd': 'Shudder Amazon Channel', 'amu': 'Mubi Amazon Channel', 'aac': 'AcornTV Amazon Channel', 'abb': 'BritBox Amazon Channel', 'afa': 'Fandor Amazon Channel', 'asb': 'Screambox Amazon Channel', 'asn': 'Sundance Now Amazon Channel', 'ctw': 'Cartoon Network', 'ads': 'Adult Swim', 'usn': 'USA Network', 'fus': 'Fox', 'fxf': 'FlixFling', 'bpc': 'Bet+ Amazon Channel', 'vik': 'Rakuten Viki', 'amo': 'AMC on Demand', 'dkm': 'Darkmatter TV', 'tcm': 'TCM', 'brv': 'Bravo TV', 'tnt': 'TNT', 'fnw': 'Food Network', 'bca': 'BBC America', 'ind': 'IndieFlix', 'ahc': 'AHCTV', 'tlc': 'TLC', 'hgt': 'HGTV', 'diy': 'DIY Network', 'inv': 'Investigation Discovery', 'sci': 'Science Channel', 'dea': 'Destination America', 'apl': 'Animal Planet', 'dil': 'Discovery Life', 'dis': 'Discovery', 'mtr': 'Motor Trend', 'coo': 'Cooking Channel', 'tra': 'Travel Channel', 'pnw': 'Paramount Network', 'hrv': 'Here TV', 'tvl': 'TV Land', 'ltv': 'Logo TV', 'vho': 'VH1', 'fpm': 'Flix Premiere', 'adw': 'DreamWorksTV Amazon Channel', 'tus': 'TBS', 'asc': 'AsianCrush', 'flr': 'FILMRISE', 'rvy': 'Revry', 'dsv': 'DOCSVILLE', 'rst': 'Rooster Teeth', 'sod': 'Spectrum On Demand', 'oxy': 'OXYGEN', 'hyh': 'Hi-YAH', 'vrv': 'VRV', 'tru': 'tru TV', 'dnw': 'DisneyNOW', 'wet': 'WeTV', 'dpu': 'Discovery Plus', 'awp': 'ARROW', 'plx': 'Plex', 'wow': 'WOW Presents Plus', 'alm': 'Alamo on Demand', 'mgl': 'Magellan TV', 'bhd': 'BroadwayHD', 'own': 'The Oprah Winfrey Network', 'fmz': 'Filmzie', 'mvt': 'MovieSaints', 'dog': 'Dogwoof On Demand', 'trs': 'True Story', 'mst': 'Martha Stewart TV', 'daf': 'DocAlliance Films', 'bph': 'British PathÃ© TV', 'kor': 'KoreaOnDemand', 'hoc': 'Hoichoi', 'fmp': 'Film Movement Plus', 'iqi': 'iQIYI', 'mtg': 'Metrograph', 'aim': 'IMDB TV Amazon Channel', 'cur': 'Curia', 'pdm': 'Public Domain Movies', 'knw': 'Kino Now'}
just_watch = JustWatch(country='US')
paid_services = ['amp', 'nfx', 'stv'] # set streaming services to search (in order)
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
print(letterboxd_username+"'s watchlist: "+str(watchlist_titles))


result = {}
for i in range(len(watchlist_titles)):
	movie = watchlist_titles[i]
	movies_found = just_watch.search_for_item(query=movie, monetization_types=['flatrate', 'free', 'ads'])
	if len(movies_found['items'])>0 and movies_found['items'][0]['title'] == movie:
		movie_found = False
		for offer in movies_found['items'][0]['offers']:
			if offer['monetization_type']=='flatrate' and offer['package_short_name'] in paid_services:
				movie_found = True
				try:
					result[service_codes[offer['package_short_name']]].append(movie+' ('+str(movies_found['items'][0]['original_release_year'])+')')
				except:
					result[service_codes[offer['package_short_name']]] = [movie+' ('+str(movies_found['items'][0]['original_release_year'])+')']
				break
			elif offer['monetization_type'] in ['free','ads']:
				movie_found = True
				try:
					result['Free Services'].append(service_codes[offer.get('package_short_name')]+': '+movie+' ('+str(movies_found['items'][0]['original_release_year'])+')')
				except:
					result['Free Services'] = [service_codes[offer.get('package_short_name')]+': '+movie+' ('+str(movies_found['items'][0]['original_release_year'])+')']
				break
		if not movie_found:
			try:
				result['F2Movies'].append(movie+' ('+str(movies_found['items'][0]['original_release_year'])+')')
			except:
				result['F2Movies'] = [movie+' ('+str(movies_found['items'][0]['original_release_year'])+')']


pprint(result)