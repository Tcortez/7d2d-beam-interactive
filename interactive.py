import asyncio, requests, os, random
from beam_interactive import start
from beam_interactive import proto


def test(streamer, steamid, server):

	# Beam Interactive Login
	path = "https://beam.pro/api/v1"
	streamer = streamer
	server = server

	# Path to Python.. can be python2.7 or above for this entry
	# PYTHON_PATH = '<PATH_TO_PYTHON>';

	# Path to Python Telnet Script - USE "/" as separator even on Windows
	PYSCRIPT_PATH = './telnet.py'

	# 7 Days to Die Player Name
	steam = steamid['playerid']

	# os.system('python {} {} {} {}'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password']))

	# Spawn Lists
	# items = [ITEM, QUANTITY]
	items = [
		['gunPistol', 1],
		['gunPumpShotgun', 1],
		['gunSawedOffPumpShotgun', 1],
		['gunAK47', 1],
		['gun44Magnum', 1],
		['gunHuntingRifle', 1],
		['gunSniperRifle', 1],
		['nailgun', 1],
		['shotgunShell', 20],
		['shotgunSlug', 20],
		['10mmBullet', 20],
		['9mmBullet', 20],
		['762mmBullet', 20],
		['44MagBullet', 20],
		['miningHelmet', 1]
	]

	enemies = [
		'zombieSteve',
		'zombieBoe',
		'zombieMoe',
		'zombieJoe',
		'zombieArlene',
		'zombieDarlene',
		'zombieMarlene',
		'zombieSteveCrawler',
		'animalBear'
	]

	friends = [
		'animalRabbit',
		'animalChicken',
		'animalStag',
		'animalPig'
	]

	# Random range of numbers
	num = random.randrange(0, 100)

	###################################################################################
	# ##########################   NO EDIT BELOW THIS LINE   ######################## #
	###################################################################################

	loop = asyncio.get_event_loop()


	class AuthenticationException(Exception):
		def __init__(self, value):
			self.parameter = value

		def __str__(self):
			return repr(self.parameter)


	class Beam:
		@staticmethod
		def get_tetris(session, channel):
			"""
			:param session:
			:param channel:
			:return:
			"""
			"""Retrieve interactive connection information."""
			return session.get(path + "/tetris/{id}/robot".format(id=channel)).json()

		@staticmethod
		def go_interactive(session, channel_id, version, code):
			interactiveDetails = dict(tetrisGameId=version, tetrisShareCode=code, interactive=1)
			return session.put(path + "/channels/{id}".format(id=channel_id), interactiveDetails).json()

		@staticmethod
		def on_handshake():
			print("Shaking hands\n")

		@staticmethod
		def on_handshake_ack(decoded):
			decoded
			print("Shaken hands\n")

		@staticmethod
		def on_error(error):
			"""
			:param error:
			:return:
			"""
			"""This is called when we get an Error packet. It contains
			a single attribute, 'message'.
			"""
			print('Oh no, there was an error!\n')
			print(error.message)

		@staticmethod
		def login(session, username, password):
			"""
			:param session:
			:param username:
			:param password:
			:return:
			"""
			"""Log into the Beam servers via the API."""
			user = dict(username=username, password=password)
			return session.post(path + "/users/login", user).json()

		@staticmethod
		def on_report(report):

			# Example of how to parse the reports
			for tactile in report.tactile:

				# Spawn Animal
				if tactile.pressFrequency > 0 and tactile.id == 0:
					key = random.randrange(0, len(friends))
					os.system('python {} {} {} {} 3 spawnentity {} {}'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password'], steam, friends[key]))

				# Spawn Enemy
				elif tactile.pressFrequency > 0 and tactile.id == 1:
					key = random.randrange(0, len(enemies))
					if num == 73:
						os.system('python {} {} {} {} 2 spawnwanderinghorde'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password']))
					else:
						os.system('python {} {} {} {} 2 spawnentity {} {}'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password'], steam, enemies[key]))

				# Spawn Item
				elif tactile.pressFrequency > 0 and tactile.id == 2:
					key = random.randrange(0, len(items))
					if num == 73:
						os.system('python {} {} {} {} 1 spawnairdrop'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password']))
					else:
						os.system('python {} {} {} {} 4 give {} {} {}'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password'], steam, items[key][0], items[key][1]))

				# Spawn Horde
				elif tactile.pressFrequency > 0 and tactile.id == 3:
					os.system('python {} {} {} {} 2 spawnwanderinghorde'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password']))

				# Spawn Feral
				elif tactile.pressFrequency > 0 and tactile.id == 4:
					os.system('python {} {} {} {} 2 spawnentity {} zombieFeral'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password'], steam))

				elif tactile.pressFrequency > 0 and tactile.id == 5:
					os.system('python {} {} {} {} 2 spawnentity {} zombieScreamer'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password'], steam))

				# Spawn Airdrop
				elif tactile.pressFrequency > 0 and tactile.id == 6:
					os.system('python {} {} {} {} 1 spawnairdrop'.format(PYSCRIPT_PATH, server['host'], server['port'], server['password']))

		@asyncio.coroutine
		def connect(self, user):
			session = requests.Session()
			channel_data = Beam().login(session, **user)

			if "channel" not in channel_data:
				raise AuthenticationException("Incorrect username or password\n")

			channel_id = channel_data["channel"]["id"]
			data = Beam().get_tetris(session, channel_id)
			# interactiveData = Beam().go_interactive(session, channel_id, game_version, share_code)
			conn = yield from start(data['address'], channel_id, data['key'], loop)
			print("Using channel ID: ", channel_id, "\n")

			# Handlers definitions
			handlers = {
				proto.id.error: Beam().on_error,
				proto.id.report: Beam().on_report,
				proto.id.handshake: Beam().on_handshake,
				proto.id.handshake_ack: Beam().on_handshake_ack
			}

			# Actual parsing of the received packet
			while (yield from conn.wait_message()):
				decoded, packet_bytes = conn.get_packet()
				packet_id = proto.id.get_packet_id(decoded)
				if decoded is None:
					print('We got a bunch of unknown bytes.')
				elif packet_id in handlers:
					handlers[packet_id](decoded)
				else:
					print("We got packet {} but didn't handle it!".format(packet_id))
					print("Closing\n")
					conn.close()

	# Create another object like this to add another player
	player = Beam()

	try:
		# Do a new line similar to this line but with objects for the new player
		asyncio.async(player.connect(streamer))
		loop.run_forever()
	except KeyboardInterrupt:
		print("Disconnected.")
	finally:
		loop.close()
