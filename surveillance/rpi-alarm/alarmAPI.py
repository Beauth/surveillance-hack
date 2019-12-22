

import RPi.GPIO as GPIO
import threading
import time
import json
from flask import Flask, render_template, request, Response,jsonify 

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
triggered = False

thread = threading.Thread()
thread.daemon = False

# Dictionary used to store the pin number, name, and pin state:
pins = {
   26 : {'name' : 'alarm', 'state' : GPIO.LOW},
   13 : {'name' : 'siren', 'state' : GPIO.LOW},
   19 : {'name' : 'active', 'state' : GPIO.HIGH}
   }

alarm_state = {'state': 0, 'triggered': triggered}
# Set each pin as an output and set it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, pins[pin]['state'])

@app.route("/", methods = ['GET','POST'])
def main():
   """Returns alarms current state"""
    global alarm_state
    global triggered
    if request.method == 'POST':
	    password = request.form.get('password')
	    if password == 'admin':		   
		    alarm_state['state'] = GPIO.input(13)
		    alarm_state['triggered'] = triggered
		    return jsonify(alarm_state)
	    else:
		    return 'Access Denied'
		   
@app.route("/change_state", methods = ['GET','POST'])
def change_state():
	"""Changes alarm's current state"""
    global triggered 
    global alarm_state
    if request.method == 'POST':
	    password = request.form.get('password')
	    if password == 'admin':	
	        GPIO.output(13, not GPIO.input(13))
		    if GPIO.input(13) == 0:
			    triggered = False			 	
		    alarm_state['state'] = GPIO.input(13)
		    alarm_state['triggered'] = triggered
		    return jsonify(alarm_state)
	    else:
		    return 'Access Denied'
		   
@app.route("/trigger", methods = ['GET','POST'])
def trigger():
   """Triggers the alarm"""
   global triggered
   if request.method == 'POST':
	   password = request.form.get('password')
	   if password == 'admin':
		   GPIO.output(26, GPIO.HIGH)
		   triggered = True	
		   global thread    
		   
		   if not thread.isAlive():
			   thread = threading.Thread(name='trigger_thread', target = alarmtrigger,args=())
			   thread.start()			   
		   alarm_state['state'] = GPIO.input(13)
		   alarm_state['triggered'] = triggered
		   
		   return jsonify(alarm_state)
	   else:
		   return 'Access Denied'

def alarmtrigger():
	global triggered
	while True:
		if triggered == True:	
			 GPIO.output(26, not GPIO.input(26))
			 time.sleep(0.25)
		else:
			GPIO.output(26, GPIO.LOW)
			time.sleep(1)
  
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=False)
