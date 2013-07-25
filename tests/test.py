import attendly


try:
	# Login
	user = attendly.User.login('bobby7','password')

	attendly.apikey(user['apikey'])

	# Get a list of events
	events = attendly.Event.list()
	for e in events:
		print e['event']['name']

	# Get an event
	event = attendly.Event.get(events[0]['event']['id'])
	print event['url']

except attendly.AttendlyError, e:
	print e.message