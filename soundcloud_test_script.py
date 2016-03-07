import soundcloud
import pprint
import time

# # create client object with app credentials
# client = soundcloud.Client(client_id='c892b76c132acff5771cb267a7e5a618',
#                            client_secret='81f6f613a5e1e9f0257d8939fe734f88',
#                            redirect_uri='http://example.com/callback')

# # redirect user to authorize URL
# redirect client.authorize_url()

# create a client object with your app credentials
client = soundcloud.Client(client_id='c892b76c132acff5771cb267a7e5a618')

# find all sounds of buskers licensed under 'creative commons share alike'
# tracks = client.get('/tracks', q='buskers', license='cc-by-sa')
# tracks = client.get('/tracks', genres='punk')

def browse_artists():
	# i = 0
	# while i < 10000:
	artist = client.get('/users', q="skrillex")
	pprint.pprint(artist[0].__dict__)
		# time.sleep(10)
		# i += 1

browse_artists()

# http://api.soundcloud.com/resolve.json?url=http://soundcloud.com/skrillex/client_id=c892b76c132acff5771cb267a7e5a618

# https://api.soundcloud.com/users/856062.json?client_id=c892b76c132acff5771cb267a7e5a618

# song_names = set()

# most_recent = (503200, 79.414838)
# page_size = 100
# i = 0
# j = 1
# curr_time = time.clock()
# while 1:
# 	tracks = client.get('/users', q="country=germany", limit=page_size, linked_partitioning=j, offset=i*200)
# 	# tracks = client.get('/users', country="Germany")
# 	if tracks.status_code != 200:
# 		print("Received non 200 status")
# 		break
# 	if not hasattr(tracks, "next_href"):
# 		print("That's it")
# 		j += 1
# 		i = 0
# 	for track in tracks.collection:
# 		song_names.add(track)


# 	# for track in tracks.collection:
# 	# 	print track.title
# 	i += 1
# 	# print(tracks.next_href)

# 	# for track in tracks:
# 		# print(track.genre)
# 	print(len(song_names))


# print("Final", len(song_names), "found, expected", i*200, time.clock() - curr_time)
