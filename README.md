# Robosapien
Pi Zero control of Robosapien v.1

Circuit diagrams: http://markcra.com/blog/?page_id=52
Hardware mods based upon: https://fortoffee.org.uk/2016/06/embedding-a-pizero-in-a-robosapien/

Hardware mods by me

Left eye blink:
GPIO19 (set as current sink) connected via a 330 ohm  to (in parallel)  -- Left eye LED 1
                                                                        -- Left eye LED 2
                                                                        -- Left eye LED 3 (all three LEDs disconnected from motherboard)
'Rosebud' shutdown:
GPIO12 (set as input) connected via 2k7 to VRE pin on 'HEAD' connector

The software is also heavily borrowed from https://fortoffee.org.uk/2016/06/embedding-a-pizero-in-a-robosapien/ and my grateful thanks goes to Carl Monk for all his work!

'robo.py' defines the command codes and outputs the appropriate pulses to the IR receiver on the Robosapien.  It's been expanded by me to include the total command set.

RC.py is my own work, intended to be run as a 'master' programme for commanding the Robosapien.  It can take multiple commands, allowing a chain of actions to be executed.  I call it from a 'Tasker' control panel on my Android tablet. 

The Pi Zero also runs a Python script (Shutdown.py) on startup  which looks for a falling edge on GPIO12. GPIO12 is connected to the VRE pin on the Robosapien head connector.  This signal sits at 3v3 when the Robosapien is powered up, but falls to zero when the 'Rosebud' shutdown command is acted upon.  'Shutdown' runs a 'sudo shutdown -h now' on detection of this falling edge.  
The script is run at boot using systemd - the 'unit file' is called myshutdown.service and is in the /lib/systemd/system directory.

If the Pi starts randomly shutting down, check the wire to GPIO12 is still connected to the Robosapien cct board (it fell off recently and caused shutdowns about a minute from startup).

The speaker has been quietened by the addition of a couple of resistors. A relay on GPIO18 shorts one of the resistors out causing an almost return to full volume (see 'quiet.py' & 'loud.py'). In other words, the Robosapien default volume is now quiet and the 'loud.py' script has to be run to restore full volume. 'quiet.py' opens the relay to quieten things down again.

Background info. covering control via Arduino:  https://playground.arduino.cc/Main/RoboSapienIR/


