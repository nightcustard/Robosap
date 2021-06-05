# Robosapien
Pi Zero control of Robosapien v.1

Circuit diagrams: http://markcra.com/blog/?page_id=52
Hardware mods based upon: https://fortoffee.org.uk/2016/06/embedding-a-pizero-in-a-robosapien/

The software is also heavily borrowed from https://fortoffee.org.uk/2016/06/embedding-a-pizero-in-a-robosapien/ and my grateful thanks goes to Carl Monk for all his work!

'robo.py' is the main programme run as a service from startup (see the 'fortoffee' write up).  It's been expanded by me to include the total command set.

The Pi Zero runs a Python script (Shutdown.py) on startup  which looks for a falling edge on GPIO12. GPIO12 is connected to the VRE pin on the Robosapien head connector.  This signal sits at 3v3 when the Robosapien is powered up, but falls to zero when the 'Rosebud' shutdown command is acted upon.  'Shutdown' runs a 'sudo shutdown -h now' on detection of this falling edge.  
The script is run at boot using systemd - the 'unit file' is called myshutdown.service and is in the /lib/systemd/system directory.

If the Pi starts randomly shutting down, check the wire to GPIO12 is still connected to the Robosapien cct board (it fell off recently and caused shutdowns about a minute from startup).

The speaker has been quietened by the addition of a couple of resistors. A relay on GPIO18 shorts one of the resistors out causing an almost return to full volume (see 'quiet.py' & 'loud.py'). In other words, the Robosapien default volume is now quiet and the 'loud.py' script has to be run to restore full volume. 'quiet.py' opens the relay to quieten things down again.

Background info. covering control via Arduino:  https://playground.arduino.cc/Main/RoboSapienIR/


