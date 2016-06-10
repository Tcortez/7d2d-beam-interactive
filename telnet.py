import telnetlib, sys, re, time

# Games server info
server = dict(host=sys.argv[1], port=sys.argv[2], password=sys.argv[3])
print(server)

host = server['host']
port = server['port']
password = server['password']

# Chat Dictionary
chat = {
	1: 'AIR DROP INCOMING!!',
	2: ' SPAWNING IN 10!!',
	3: 'WATCH OUT... there is a WILD',
	4: 'LOOK DOWN... Someone gave you'
}

# List of words to filter out for prettier wording
itemList = [
	'gun',
	'animal',
	'zombie',
	'bear'
]

########################################################################
# ####################### NO EDIT PAST THIS LINE ##################### #
########################################################################

# Test if args supplied
if len(sys.argv) < 2:
	print('ERROR: No args supplied')
	sys.exit()

# Get the game command
cmdList = []

# Loop through args provided
# Add to the cmdList list for storage
for x in sys.argv:
	cmdList.append(x)

print(cmdList)
# Store arg for chat logic
whatToSay = int(cmdList[4])

# Placeholders
user = ''
item = cmdList[2]

# Check if we have a user in args
if len(sys.argv) > 6:
	user = cmdList[6]

# checks to see if we have enough args supplied for an item to be given
if len(sys.argv) > 7:
	item = cmdList[7].upper()

	# Search list and remove ugly words
	for a in itemList:
		if re.match('^'+a+'', item, flags=re.IGNORECASE):
			if a == 'zombie' or a == 'bear':
				item = re.sub('^'+a+'', ' '+a.upper()+' ', item, flags=re.IGNORECASE)
			item = re.sub('^'+a+'', '', item, flags=re.IGNORECASE)

# Remove the first and second element as it is not needed past here
cmdList.pop(0)
cmdList.pop(0)
cmdList.pop(0)
cmdList.pop(0)
cmdList.pop(0)
# Convert the list into a string separated by a space
cmd = ' '.join(cmdList)

print(cmd)

# connect to remote host
try:
	tn = telnetlib.Telnet(host, port)
except:
	print('Unable to connect')
	sys.exit()

# Send Password
tn.read_until('Password: ', 2)
tn.write(password + '\n')

# BASIC Say something in game when button pressed
# Will make this more robust in the future
if whatToSay == 1:
	tn.write('say " ' + chat[1] + '" \n')
elif whatToSay == 2:
	if item == 'spawnwanderinghorde':
		tn.write('say "WANDERING HORDE INCOMING" \n')
	else:
		tn.write('sayPlayer ' + user + ' "' + item + chat[2] + '" \n')
		time.sleep(10)
elif whatToSay == 3:
	tn.write('sayPlayer ' + user + ' "' + chat[3] + ' ' + item + ' around you!" \n')
elif whatToSay == 4:
	if item == "WOOD":
		tn.write('sayPlayer ' + user + ' "' + chat[4] + ' some ' + item + '!" \n')
	else:
		tn.write('sayPlayer ' + user + ' "' + chat[4] + ' a ' + item + '!" \n')
else:
	print('OOPS!!')
	sys.exit()

# Send the command to the game server
tn.write(cmd + '\n')

# Exit Python Script
sys.exit()

# Allow interaction with telnet
tn.mt_interact()
