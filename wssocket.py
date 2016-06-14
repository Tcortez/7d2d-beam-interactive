import websocket
import _thread as thread
import time
import sys
import json


def on_message(ws, message):
	response = json.loads(message)
	print(response, "\n")

	data = []
	# if event is command store the rawcommand, username, userid
	# in the data list for use later
	if response['event'] == 'cmdran':
		data.append(response['data']['rawcommand'])
		data.append(response['data']['username'])
		data.append(response['data']['userid'])

	# see what is in the data list
	print("\nDATA: ", data)


# if error is thrown
def on_error(ws, error):
	print(error)


# if connection is closed
def on_close(ws):
	print("### closed ###")


# open the connection
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

		# send the auth and sub data
		ws.send(json.dumps(auth))
		ws.send(json.dumps(sub))

		# keep sending to keep the connection open
		while True:
			time.sleep(50)
			ws.send(json.dumps(auth))

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
