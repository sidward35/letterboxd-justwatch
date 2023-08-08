# letterboxd-justwatch

Try the web version at [js.smathur.xyz](https://js.smathur.xyz)!

Scans your [Letterboxd](https://letterboxd.com) watchlist and shows you where you can watch those movies using [JustWatch](https://www.justwatch.com).

Like this project? Support me below:

<a href="https://www.paypal.com/donate/?business=ZBR8BGKVU5C5C&no_recurring=1">
  <img src="https://user-images.githubusercontent.com/8982949/33011169-6da4af5e-cddd-11e7-94e5-a52d776b94ba.png" />
</a>

## Usage
1. Install `BeautifulSoup4` and `justwatch` using pip.
2. Download [movie_finder_optimized.py](https://raw.githubusercontent.com/sidward35/letterboxd-justwatch/main/movie_finder_optimized.py).
3. Edit lines 10 and 11 to set your paid streaming services ([service codes](#service-codes) below) and Letterboxd username.
```python
paid_services = ['amp', 'nfx', 'stv']
letterboxd_username = 'sidward35'
```
4. Run `python movie_finder_optimized.py`

## Service Codes
|Streaming Service|Code|
|:-:|:-:|
|A&E|aae|
|ABC|abc|
|AHCTV|ahc|                                     |AMC|amc|
|AMC Plus|azp|                                  |AMC Theatres|amt|
|AMC on Demand|amo|
|AMC+ Roku Premium Channel|ark|
|ARROW|awp|
|Acorn TV|act|
|AcornTV Amazon Channel|aac|
|Adult Swim|ads|
|Alamo on Demand|alm|
|Amazon Prime Video|amp|
|Amazon Video|amz|
|Animal Planet|apl|
|Apple TV Plus|atp|
|Apple iTunes|itu|
|AsianCrush|asc|
|BBC America|bca|
|Bet+ Amazon Channel|bpc|
|Boomerang|bmg|
|Boomerang Amazon Channel|abo|
|Bravo TV|brv|
|BritBox|bbo|
|BritBox Amazon Channel|abb|
|British PathÃ© TV|bph|
|BroadwayHD|bhd|
|The CW|tcw|
|CW Seed|cws|
|Cartoon Network|ctw|
|Chai Flicks|chf|
|Cinemax Amazon Channel|acn|
|Classix|cla|
|Comedy Central|com|
|Cooking Channel|coo|
|Crackle|crk|
|Criterion Channel|crc|
|Crunchyroll|cru|
|Curia|cur|
|Curiosity Stream|cts|
|DIRECTV|drv|
|DIY Network|diy|
|DOCSVILLE|dsv|
|Darkmatter TV|dkm|
|Dekkoo|dkk|
|Destination America|dea|
|Discovery|dis|
|Discovery Life|dil|
|Discovery Plus|dpu|
|Discovery+ Amazon Channel|adp|
|Disney Plus|dnp|
|DisneyNOW|dnw|
|DocAlliance Films|daf|
|Dogwoof On Demand|dog|
|Dove Channel|dvc|
|DreamWorksTV Amazon Channel|adw|
|EPIX Amazon Channel|aep|
|Epix|epx|
|Epix Roku Premium Channel|erk|
|Eros Now|ern|
|FILMRISE|flr|
|FXNow|fxn|
|Fandor|fnd|
|Fandor Amazon Channel|afa|
|The Film Detective|tfd|
|Film Movement Plus|fmp|
|Filmzie|fmz|
|Flix Premiere|fpm|
|FlixFling|fxf|
|Food Network|fnw|
|Fox|fus|
|Freeform|ffm|
|fuboTV|fuv|
|Funimation Now|fmn|
|Google Play Movies|ply|
|GuideDoc|gdc|
|HBO Max|hbm|
|HBO Max Free|hmf|
|HBO Now|hbn|
|HBO Now Amazon Channel|ahb|
|HGTV|hgt|
|Hallmark Movies|hmm|
|Hallmark Movies Now Amazon Channel|ahm|
|Here TV|hrv|
|Hi-YAH|hyh|
|HiDive|hdv|
|History|his|
|History Vault|hvt|
|Hoichoi|hoc|
|Hoopla|hop|
|Hopster TV|htv|
|Hulu|hlu|
|IMDB TV Amazon Channel|aim|
|IndieFlix|ind|
|Investigation Discovery|inv|
|iQIYI|iqi|
|Kanopy|knp|
|Kino Now|knw|
|Kocowa|koc|
|KoreaOnDemand|kor|
|Laugh Out Loud|lol|
|Lifetime|lft|
|Lifetime Movie Club|lmc|
|Logo TV|ltv|
|MTV|mtv|
|MZ Choice Amazon Channel|ame|
|Magellan TV|mgl|
|Magnolia Selects|mns|
|Martha Stewart TV|mst|
|Max Go|mxg|
|Metrograph|mtg|
|Mhz Choice|mhz|
|Microsoft Store|msf|
|Motor Trend|mtr|
|MovieSaints|mvt|
|Mubi|mbi|
|Mubi Amazon Channel|amu|
|MyOutdoorTV|mot|
|NBC|nbc|
|Netflix|nfx|
|Netflix Kids|nfk|
|Nickhits Amazon Channel|anh|
|Night Flight Plus|nfp|
|Noggin Amazon Channel|ang|
|The Oprah Winfrey Network|own|
|OVID|ovi|
|OXYGEN|oxy|
|Paramount+ Showtime|pst|
|PBS|pbs|
|PBS Kids Amazon Channel|apk|
|PBS Masterpiece Amazon Channel|apm|
|Pantaflix|pfx|
|Pantaya|pty|
|Pantaya Amazon Channel|apa|
|Paramount Network|pnw|
|Paramount Plus|pmp|
|Paramount+ Amazon Channel|app|
|Paramount+ Roku Premium Channel|prk|
|Peacock|pct|
|Peacock Premium|pcp|
|Plex|plx|
|Pluto TV|ptv|
|Popcornflix|pcf|
|Public Domain Movies|pdm|
|Pure Flix|pux|
|Rakuten Viki|vik|
|realeyz|rlz|
|Redbox|rbx|
|Retrocrush|rtc|
|Revry|rvy|
|The Roku Channel|rkc|
|Rooster Teeth|rst|
|Science Channel|sci|
|Screambox|scb|
|Screambox Amazon Channel|asb|
|Shout! Factory TV|sft|
|Showtime|sho|
|Showtime Amazon Channel|ash|
|Showtime Roku Premium Channel|srk|
|Shudder|shd|
|Shudder Amazon Channel|asd|
|Sling TV|stv|
|Smithsonian Channel|ssc|
|Spamflix|sfx|
|Spectrum On Demand|sod|
|Starz|stz|
|Starz Play Amazon Channel|ast|
|Starz Roku Premium Channel|sru|
|Sun Nxt|snx|
|Sundance Now|sdn|
|Sundance Now Amazon Channel|asn|
|Syfy|sfy|
|TBS|tus|
|TCM|tcm|
|TLC|tlc|
|TNT|tnt|
|TV Land|tvl|
|Topic|tpc|
|Travel Channel|tra|
|tru TV|tru|
|True Story|trs|
|Tubi TV|tbv|
|USA Network|usn|
|Urban Movie Channel|umc|
|VH1|vho|
|VIX |vix|
|VRV|vrv|
|VUDU Free|vuf|
|Vice TV |vtv|
|Viewster Amazon Channel|avt|
|Vudu|vdu|
|WOW Presents Plus|wow|
|WWE Network|wwe|
|WeTV|wet|
|YouTube|yot|
|YouTube Free|yfr|
|YouTube Premium|ytr|
|Yupp TV|ytv|
