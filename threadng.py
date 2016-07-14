import threading			#threading doesn't follow the logical order of the commands
					#like messenger

class Messenger(threading.Thread):			#inherited
	def run(self):
		for _ in range(10):
			print(threading.currentThread().getName())

x=Messenger(name="Sending Message")
y=Messenger(name="Receiving Message")

x.start()
y.start()
		 
