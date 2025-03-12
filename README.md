# letterboxd-justwatch

Try the web version at [js.smathur.xyz](https://js.smathur.xyz)!

Scans your [Letterboxd](https://letterboxd.com) watchlist and shows you where you can watch those movies using [JustWatch](https://www.justwatch.com).

## Usage
1. Install `BeautifulSoup4` and `simple-justwatch-python-api` using pip.
2. Download [movie_finder.py](https://github.com/sidward35/letterboxd-justwatch/blob/main/movie_finder.py).
3. Edit lines 11 and 17 to set your paid streaming services ([service codes](#service-codes) below) and Letterboxd username.
```python
# line 11
letterboxd_username = 'sidward35'
# line 17
paid_services = [9, 8, 299]  # Amazon Prime, Netflix, Sling TV
```
4. Run `python movie_finder.py`

## Service Codes
| Streaming Service | Code | Provider ID |
|:----------------:|:----:|:-----------:|
| A&E | aae | 156 |
| ABC | abc | 148 |
| AHCTV | ahc | 398 |
| AMC | amc | 80 |
| AMC Plus | azp | 528 |
| AMC Theatres | amt | 162 |
| AMC on Demand | amo | 352 |
| AMC+ Roku Premium Channel | ark | 635 |
| ARROW | awp | 529 |
| Acorn TV | act | 87 |
| AcornTV Amazon Channel | aac | 196 |
| Adult Swim | ads | 318 |
| Alamo on Demand | alm | 547 |
| Amazon Prime Video | amp | 9 |
| Amazon Video | amz | 10 |
| Animal Planet | apl | 399 |
| Apple TV Plus | atp | 350 |
| Apple iTunes | itu | 2 |
| AsianCrush | asc | 514 |
| BBC America | bca | 397 |
| Bet+ Amazon Channel | bpc | 343 |
| Boomerang | bmg | 248 |
| Boomerang Amazon Channel | abo | 288 |
| Bravo TV | brv | 365 |
| BritBox | bbo | 151 |
| BritBox Amazon Channel | abb | 197 |
| British Pathé TV | bph | 571 |
| BroadwayHD | bhd | 554 |
| The CW | tcw | 83 |
| CW Seed | cws | 206 |
| Cartoon Network | ctw | 317 |
| Chai Flicks | chf | 438 |
| Cinemax Amazon Channel | acn | 289 |
| Classix | cla | 445 |
| Comedy Central | com | 243 |
| Cooking Channel | coo | 400 |
| Crackle | crk | 12 |
| Criterion Channel | crc | 258 |
| Crunchyroll | cru | 283 |
| Curia | cur | 617 |
| Curiosity Stream | cts | 190 |
| DIRECTV | drv | 358 |
| DIY Network | diy | 405 |
| DOCSVILLE | dsv | 475 |
| Darkmatter TV | dkm | 355 |
| Dekkoo | dkk | 444 |
| Destination America | dea | 402 |
| Discovery | dis | 403 |
| Discovery Life | dil | 404 |
| Discovery Plus | dpu | 520 |
| Discovery+ Amazon Channel | adp | 584 |
| Disney Plus | dnp | 337 |
| DisneyNOW | dnw | 508 |
| DocAlliance Films | daf | 569 |
| Dogwoof On Demand | dog | 536 |
| Dove Channel | dvc | 254 |
| DreamWorksTV Amazon Channel | adw | 263 |
| EPIX Amazon Channel | aep | 583 |
| Epix | epx | 34 |
| Epix Roku Premium Channel | erk | 636 |
| Eros Now | ern | 218 |
| FILMRISE | flr | 471 |
| FXNow | fxn | 123 |
| Fandor | fnd | 25 |
| Fandor Amazon Channel | afa | 199 |
| The Film Detective | tfd | 470 |
| Film Movement Plus | fmp | 579 |
| Filmzie | fmz | 559 |
| Flix Premiere | fpm | 432 |
| FlixFling | fxf | 331 |
| Food Network | fnw | 366 |
| Fox | fus | 328 |
| Freeform | ffm | 211 |
| Freevee | aim | 613 |
| fuboTV | fuv | 257 |
| Funimation Now | fmn | 269 |
| Google Play Movies | ply | 3 |
| GuideDoc | gdc | 100 |
| HBO Max | hbm | 384 |
| HBO Max Free | hmf | 616 |
| HBO Now | hbn | 27 |
| HBO Now Amazon Channel | ahb | 200 |
| HGTV | hgt | 406 |
| Hallmark Movies | hmm | 281 |
| Hallmark Movies Now Amazon Channel | ahm | 290 |
| Here TV | hrv | 417 |
| Hi-YAH | hyh | 503 |
| HiDive | hdv | 430 |
| History | his | 155 |
| History Vault | hvt | 268 |
| Hoichoi | hoc | 315 |
| Hoopla | hop | 212 |
| Hopster TV | htv | 267 |
| Hulu | hlu | 15 |
| IMDB TV Amazon Channel | aim | 613 |
| IndieFlix | ind | 368 |
| Investigation Discovery | inv | 408 |
| iQIYI | iqi | 581 |
| Kanopy | knp | 191 |
| Kino Now | knw | 640 |
| Kocowa | koc | 464 |
| KoreaOnDemand | kor | 575 |
| Laugh Out Loud | lol | 275 |
| Lifetime | lft | 157 |
| Lifetime Movie Club | lmc | 284 |
| Logo TV | ltv | 420 |
| MTV | mtv | 453 |
| MZ Choice Amazon Channel | ame | 291 |
| Magellan TV | mgl | 551 |
| Magnolia Selects | mns | 259 |
| Martha Stewart TV | mst | 568 |
| Max Go | mxg | 139 |
| Metrograph | mtg | 585 |
| Mhz Choice | mhz | 427 |
| Microsoft Store | msf | 68 |
| Motor Trend | mtr | 410 |
| MovieSaints | mvt | 562 |
| Mubi | mbi | 11 |
| Mubi Amazon Channel | amu | 201 |
| MyOutdoorTV | mot | 264 |
| NBC | nbc | 79 |
| Netflix | nfx | 8 |
| Netflix Kids | nfk | 175 |
| Nickhits Amazon Channel | anh | 261 |
| Night Flight Plus | nfp | 455 |
| Noggin Amazon Channel | ang | 262 |
| The Oprah Winfrey Network | own | 555 |
| OVID | ovi | 433 |
| OXYGEN | oxy | 487 |
| Paramount+ Showtime | pst | - |
| PBS | pbs | 209 |
| PBS Kids Amazon Channel | apk | 293 |
| PBS Masterpiece Amazon Channel | apm | 294 |
| Pantaflix | pfx | 177 |
| Pantaya | pty | 247 |
| Pantaya Amazon Channel | apa | 292 |
| Paramount Network | pnw | 418 |
| Paramount Plus | pmp | 531 |
| Paramount+ Amazon Channel | app | 582 |
| Paramount+ Roku Premium Channel | prk | 633 |
| Peacock | pct | 386 |
| Peacock Premium | pcp | 387 |
| Plex | plx | 538 |
| Pluto TV | ptv | 300 |
| Popcornflix | pcf | 241 |
| Public Domain Movies | pdm | 638 |
| Pure Flix | pux | 278 |
| Rakuten Viki | vik | 344 |
| realeyz | rlz | 14 |
| Redbox | rbx | 279 |
| Retrocrush | rtc | 446 |
| Revry | rvy | 473 |
| The Roku Channel | rkc | 207 |
| Rooster Teeth | rst | 485 |
| Science Channel | sci | 411 |
| Screambox | scb | 185 |
| Screambox Amazon Channel | asb | 202 |
| Shout! Factory TV | sft | 439 |
| Showtime | sho | 37 |
| Showtime Amazon Channel | ash | 203 |
| Showtime Roku Premium Channel | srk | 632 |
| Shudder | shd | 99 |
| Shudder Amazon Channel | asd | 204 |
| Sling TV | stv | 299 |
| Smithsonian Channel | ssc | 276 |
| Spamflix | sfx | 521 |
| Spectrum On Demand | sod | 486 |
| Starz | stz | 43 |
| Starz Play Amazon Channel | ast | 194 |
| Starz Roku Premium Channel | sru | 634 |
| Sun Nxt | snx | 309 |
| Sundance Now | sdn | 143 |
| Sundance Now Amazon Channel | asn | 205 |
| Syfy | sfy | 215 |
| TBS | tus | 506 |
| TCM | tcm | 361 |
| TLC | tlc | 412 |
| TNT | tnt | 363 |
| TV Land | tvl | 419 |
| Topic | tpc | 454 |
| Travel Channel | tra | 413 |
| tru TV | tru | 507 |
| True Story | trs | 567 |
| Tubi TV | tbv | 73 |
| USA Network | usn | 322 |
| Urban Movie Channel | umc | 251 |
| VH1 | vho | 422 |
| VIX | vix | 457 |
| VRV | vrv | 504 |
| VUDU Free | vuf | 332 |
| Vice TV | vtv | 458 |
| Viewster Amazon Channel | avt | 295 |
| Vudu | vdu | 7 |
| WOW Presents Plus | wow | 546 |
| WWE Network | wwe | 260 |
| WeTV | wet | 509 |
| YouTube | yot | 192 |
| YouTube Free | yfr | 235 |
| YouTube Premium | ytr | 188 |
| Yupp TV | ytv | 255 |
