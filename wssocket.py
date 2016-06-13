import websocket
try:
    import thread
except ImportError:  # TODO use Threading instead of _thread in python3
    import _thread as thread
import time
import sys
import json
import threading



def on_message(ws, message):
	response = json.loads(message)
	print(response, "\n")
	
	cmdlist = {}
	
	cost = {}
	data = []
	
	i = 0
	for a in response['data']:
		#i + 1
		#data[i] = i 
		c = {
			'comcall': a["comcall"],
			'cost': a['cost']
			}
		data.append(c)
		
	print(data)
	
	for k,v in response.items():
		
		if v =="cmdran":
			for a in response['data']:
				c = {
					'comcall': a["comcall"],
					'cost': a['cost']
					}
				data.append(c)
					cmd['rawcommand'] = v[0]['rawcommand'] 
					cmd['username'] = v[0]['username']
					cmd['userid'] = v[0]['userid']
					
			print(cmd)
	
#		while k == 'data':
#			data['test'] = v[0]["comcall"]
#			
#		
#			print(data)
		
			
		
		
	

def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")




def on_open(ws):
	def run(*args):
		auth = {
			"event": "auth",
			"data": "8d49af56-fdd8-47ea-9a2c-d7711c81f229"
		}

		sub = {
			"event": "subscribe",
			"data": "commands"
		}
		
		
		
		ws.send(json.dumps(auth))
		ws.send(json.dumps(sub))
		while True:
			time.sleep(50)
			ws.send(json.dumps(auth))
		

		# ws.close()
		print("Thread terminating...")
		
	thread.start_new_thread(run, ())


if __name__ == "__main__":
	websocket.enableTrace(True)
	if len(sys.argv) < 2:
		host = "wss://api.scottybot.net/websocket/control"
	else:
		host = sys.argv[1]
	ws = websocket.WebSocketApp(host,
		on_message=on_message,
		on_error=on_error,
		on_close=on_close)
	ws.on_open = on_open
	
	ws.run_forever()
