import telnetlib
import sys
import re
import time
import random

# Games server info
server = dict(host=sys.argv[1], port=sys.argv[2], password=sys.argv[3])
# print(server)

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

# Random range of numbers
amt1 = random.randrange(1, 20)
amt2 = random.randrange(1, 10)

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

#print(cmdList)
# Store arg for chat logic
whatToSay = int(cmdList[4])

# Placeholders
user = ''
item = cmdList[5]

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

#print cmdList[-1]

if cmdList[-1] == '0':
	cmdList[-1] = '1'
	#print("=1 ", cmdList, '\n')
elif cmdList[-1] == '1':
	cmdList[-1] = str(amt1)
elif cmdList[-1] == '2':
	cmdList[-1] = str(amt2)
# Convert the list into a string separated by a space
cmd = ' '.join(cmdList)

#print(cmd)

# connect to remote host
try:
	tn = telnetlib.Telnet(host, port)
except:
	print('Unable to connect')
	sys.exit()

# Send Password
tn.read_until(b"Please enter password: ", 4)
tn.write(password.encode('ascii') + b"\n")

#print('\n\n' + item + '\n\n')
# BASIC Say something in game when button pressed
# Will make this more robust in the future
if whatToSay == 1:
	tn.write(b'say " ' + chat[1].encode('ascii') + b'" \n')
elif whatToSay == 2:
	if item == 'spawnwanderinghorde':
		tn.write(b'say "WANDERING HORDE INCOMING" \n')
	else:
		tn.write(b'sayPlayer ' + user.encode('ascii') + b' "' + item.encode('ascii') + chat[2].encode('ascii') + b'" \n')
		time.sleep(10)
elif whatToSay == 3:
	tn.write(b'sayPlayer ' + user.encode('ascii') + b' "' + chat[3].encode('ascii') + b' ' + item.encode('ascii') + b' around you!" \n')
elif whatToSay == 4:
	if item == "WOOD":
		tn.write(b'sayPlayer ' + user.encode('ascii') + b' "' + chat[4].encode('ascii') + b' some ' + item.encode('ascii') + b'!" \n')
	else:
		tn.write(b'sayPlayer ' + user.encode('ascii') + b' "' + chat[4].encode('ascii') + b' a ' + item.encode('ascii') + b'!" \n')
else:
	print('OOPS!!')
	sys.exit()

# Send the command to the game server
tn.write(cmd.encode('ascii') + b'\n')

# Exit Python Script
sys.exit()

# Allow interaction with telnet
tn.mt_interact()
