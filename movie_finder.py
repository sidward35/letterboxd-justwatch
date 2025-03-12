from pprint import pprint
import urllib.request
import ssl
import json
from bs4 import BeautifulSoup
from simplejustwatchapi.justwatch import search

# Configuration
country = 'US'
language = 'en'
letterboxd_username = 'sidward35'

# URL to the provider map JSON file (GitLab raw URL)
PROVIDER_MAP_URL = "https://raw.githubusercontent.com/sidward35/letterboxd-justwatch/refs/heads/main/provider_map.json"

# Preferred streaming services by ID
paid_services = [9, 8, 299]  # Amazon Prime, Netflix, Sling TV

def get_provider_map():
	"""Fetch the provider map from the remote URL, with fallback to local defaults"""
	try:
		# Create context for SSL
		ssl_context = ssl._create_unverified_context()
		req = urllib.request.Request(PROVIDER_MAP_URL, headers={'User-Agent': "Python Movie Finder"})
		
		# Fetch the provider map JSON
		with urllib.request.urlopen(req, context=ssl_context) as response:
			data = json.loads(response.read().decode('utf-8'))
			
			# Convert keys from strings to integers
			provider_map = {int(k): v for k, v in data['provider_map'].items()}
			return provider_map
			
	except Exception as e:
		print(f"Warning: Could not fetch provider map from {PROVIDER_MAP_URL}. Using minimal defaults.")
		print(f"Error: {e}")
		
		# Minimal fallback provider map with key streaming services
		return {
			8: "Netflix",
			9: "Amazon Prime Video",
			299: "Sling TV",
			207: "The Roku Channel",
			300: "Pluto TV",
			123: "FXNow",
			73: "Tubi TV",
			613: "Freevee",
			212: "Hoopla",
			191: "Kanopy",
			538: "Plex",
			486: "Spectrum On Demand"
		}

def get_page_count(username):
	"""Get the number of pages in the user's watchlist"""
	html_str = ''
	url = "https://letterboxd.com/"+username+"/watchlist"
	req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"}) 
	fp = urllib.request.urlopen(req)
	html_str+=fp.read().decode("utf8")
	fp.close()

	soup = BeautifulSoup(html_str, 'html.parser')
	html_objects = soup.find_all('span', {'class': 'js-watchlist-count'})
	base_str = str(html_objects[0])
	page_count = int(base_str.replace('<span class="js-watchlist-count">', '').replace('\xa0films</span>', ''))
	return int(page_count/(7*4)+1)

def get_watchlist(username):
	"""Get the Letterboxd watchlist for the given username"""
	watchlist_titles = []
	watchlist_pages = get_page_count(username)

	ssl._create_default_https_context = ssl._create_unverified_context
	html_str = ''
	for i in range(watchlist_pages):
		url = "https://letterboxd.com/"+username+"/watchlist/by/popular/page/"+str(i+1)
		req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"}) 
		fp = urllib.request.urlopen(req)
		html_str+=fp.read().decode("utf8")
		fp.close()

	soup = BeautifulSoup(html_str, 'html.parser')
	html_objects = soup.find_all('li', {'class': 'poster-container'})
	for html_object in html_objects:
		object_str = str(html_object).replace('&amp;','&')
		start_index = object_str.index('<img alt="')+10
		end_index = object_str.index('"', start_index)
		movie_name = object_str[start_index:end_index]
		watchlist_titles.append(movie_name)
	
	return watchlist_titles

def process_watchlist(watchlist_titles, provider_map, paid_services):
	"""Process the watchlist and find streaming services for each movie"""
	result = {}
	for movie in watchlist_titles:
		# Search for the movie using the API
		search_results = search(movie, country, language, 1, False)  # Get first result, include all offers
		
		if search_results and search_results[0].title == movie:
			movie_found = False
			movie_item = search_results[0]
			# Try different attribute for release year
			try:
				release_year = movie_item.production_year
			except AttributeError:
				try:
					release_year = movie_item.release_year
				except AttributeError:
					release_year = "N/A"
			
			# Check all offers for the movie
			for offer in movie_item.offers:
				# Get provider ID from the package object
				if not hasattr(offer, 'package') or not hasattr(offer.package, 'package_id'):
					continue
					
				provider_id = offer.package.package_id
				
				# Check if the offer is for streaming (flatrate)
				if offer.monetization_type == 'FLATRATE' and provider_id in paid_services:
					movie_found = True
					service_name = provider_map.get(provider_id, f"Provider {provider_id}")
					
					if service_name not in result:
						result[service_name] = []
					result[service_name].append(f"{movie} ({release_year})")
					break
					
				# Check if the offer is free or ad-supported
				elif offer.monetization_type in ['FREE', 'ADS']:
					movie_found = True
					service_name = provider_map.get(provider_id, f"Provider {provider_id}")
					
					if 'Free Services' not in result:
						result['Free Services'] = []
					result['Free Services'].append(f"{service_name}: {movie} ({release_year})")
					break
			
			# If no matching service found, add to "Other" category
			if not movie_found and movie_item.offers:
				if 'Other' not in result:
					result['Other'] = []
				result['Other'].append(f"{movie} ({release_year})")
	
	return result

def main():
	# Load provider map
	provider_map = get_provider_map()
	
	# Get watchlist
	watchlist_titles = get_watchlist(letterboxd_username)
	print(letterboxd_username+"'s watchlist: "+str(watchlist_titles))

	# Process watchlist and find streaming services
	result = process_watchlist(watchlist_titles, provider_map, paid_services)
	
	# Print results
	pprint(result)

if __name__ == "__main__":
	main()