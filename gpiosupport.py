import evdev
import select
import requests

CCW = "http://127.0.0.1:14711/commands/rotary-ccw"
CW = "http://127.0.0.1:14711/commands/rotary-cw"
SP = "http://127.0.0.1:14711/commands/start-picture"
CO = "http://127.0.0.1:14711/commands/start-collage"
PR = "http://127.0.0.1:14711/commands/print"
CU = "http://127.0.0.1:14711/commands/start-custom"
RB = "http://127.0.0.1:14711/commands/rotary-btn-press"
SD = "http://127.0.0.1:14711/commands/shutdown-now"
MUSB = "http://127.0.0.1:14711/commands/start-move2usb"

def send_request(url):

   try:
      response = requests.get(url)
      print(f"Request to {url}responded with status code: {response.status_code}")
   except requests.RequestException as e:
      print(f"Request to {url} failed: {e}")



devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
devices = {dev.fd: dev for dev in devices}
value = 1
print("Value: {0}".format(value))
done = False
while not done:
  r, w, x = select.select(devices, [], [])
  for fd in r:
   for event in devices[fd].read():
     event = evdev.util.categorize(event)
     if isinstance(event, evdev.events.RelEvent):
        value = value + event.event.value
        print("Value: {0}".format(value))
        if event.event.value == 1:
            send_request(CW)
        elif event.event.value == -1:
            send_request(CCW)
     elif isinstance(event, evdev.events.KeyEvent):
        if event.keycode == "KEY_ENTER" and event.keystate == event.key_up:
            send_request(RB)
        if event.keycode == "KEY_T" and event.keystate == event.key_up:
            send_request(SP)
        if event.keycode == "KEY_C" and event.keystate == event.key_up:
            send_request(CO)       
        if event.keycode == "KEY_P" and event.keystate == event.key_up:
            send_request(PR)
        if event.keycode == "KEY_U" and event.keystate == event.key_up:
            send_request(CU)
        if event.keycode == "KEY_S" and event.keystate == event.key_up:
            send_request(SD)
        if event.keycode == "KEY_M" and event.keystate == event.key_up:
            send_request(MUSB)              
