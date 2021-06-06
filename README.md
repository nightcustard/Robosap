# Robosapien
Pi Zero control of Robosapien v.1

Circuit diagrams: http://markcra.com/blog/?page_id=52
Hardware mods based upon: https://fortoffee.org.uk/2016/06/embedding-a-pizero-in-a-robosapien/

Hardware mods by me:

Left eye blink:
GPIO19 (set as current sink) connected via a 330 ohm  to (in parallel)  -- Left eye LED 1
                                                                        -- Left eye LED 2
                                                                        -- Left eye LED 3 (all three LEDs disconnected from motherboard)

'Rosebud' shutdown:
GPIO12 (set as input) connected via 2k7 to VRE pin on 'HEAD' connector

Photos and circuit mods can be found under 'Robosap mods' in 'Issues'.

The software is also heavily borrowed from https://fortoffee.org.uk/2016/06/embedding-a-pizero-in-a-robosapien/ and my grateful thanks goes to Carl Monk for all his work!

'robo.py' defines the command codes and outputs the appropriate pulses to the IR receiver on the Robosapien.  It's been expanded by me to include the total command set.

RC.py is my own work, intended to be run as a 'master' programme for commanding the Robosapien.  It can take multiple commands, allowing a chain of actions to be executed.  I call it from a 'Tasker' control panel on my Android tablet. 

The Pi Zero also runs a Python script (Shutdown.py) on startup  which looks for a falling edge on GPIO12. GPIO12 is connected to the VRE pin on the Robosapien head connector.  This signal sits at 3v3 when the Robosapien is powered up, but falls to zero when the 'Rosebud' shutdown command is acted upon.  'Shutdown' runs a 'sudo shutdown -h now' on detection of this falling edge.  
The script is run at boot using systemd - the 'unit file' is called myshutdown.service and is in the /lib/systemd/system directory.

If the Pi starts randomly shutting down, check the wire to GPIO12 is still connected to the Robosapien cct board (it fell off recently and caused shutdowns about a minute from startup).

The speaker has been quietened by the addition of a couple of resistors. A relay on GPIO18 shorts one of the resistors out causing an almost return to full volume (see 'quiet.py' & 'loud.py'). In other words, the Robosapien default volume is now quiet and the 'loud.py' script has to be run to restore full volume. 'quiet.py' opens the relay to quieten things down again.

Background info. covering control via Arduino:  https://playground.arduino.cc/Main/RoboSapienIR/

Software installation:

Flash the latest version of Buster light onto the Pi's SD card
  - Remember to create an empty file in the 'boot' partition called 'ssh' to turn on ssh
  - In the same partition create a wpa_supplicant.conf file with your wifi details (eg)
          country=UK
          ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
          update_config=1
          network={
                ssid="yourSSID"
                psk="yourwifipassword"
                key_mgmt=WPA-PSK
              }
Power up, wait for the Pi to finish booting and start an ssh session (eg) ssh pi@192.168.1.xx (in Linux) - use PuTTY if in Windows.
Run raspi-config to change password, set hostname and expand filesystem
Do a sudo apt update
Add .ssh/authorized_keys (if you want)
Create '~/software' folder
Install PiGPIO:
 - sudo apt install pigpio python-pigpio python3-pigpio
 Followed by:
 - sudo apt install git
 - git clone https://github.com/joan2937/pigpio
 To run PiGPIO in Python 3, you’ll need to run:
 - sudo apt install python3-rpi.gpio
 To run pigpiod on boot:
 - sudo systemctl enable pigpiod
If this doesn’t work, add this line to the system crontab (sudo crontab –e): 
 - @reboot /usr/local/bin/pigpiod
Copy RC.py, quiet.py, loud.py, robo.py & Shutdown.py to ~/software
sudo nano /boot/config.txt:  Add ‘dtparam=act_led_gpio=19’ to redirect the activity LED to GPIO 19 (the onboard LED is extinguished).
dtparam=act_led_trigger=heartbeat for regular LED pulsing.

Running Shutdown.py as a service (a service runs independently of terminal sessions):

sudo nano /lib/systemd/system/myshutdown.service
Add in the following text :

 [Unit]
 Description=myshutdown service
 After=multi-user.target

 [Service]
 Type=idle
 Restart=always
 RestartSec=0
 ExecStart=/usr/bin/python /home/pi/software/Shutdown.py
 StandardOutput=file:/home/pi/software/Shutdown_output.log
 StandardError=file:/home/pi/software/Shutdown_error.log

 [Install]
 WantedBy=multi-user.target

This defines a new service called “myshutdown service” which is launched once the multi-user environment is available. The “ExecStart” parameter is used to specify the command to run. The “Type” is set to “idle” to ensure that the ExecStart command is run only when everything else has loaded. Note that the paths are absolute and define the complete location of Python as well as the location of the Python script.

sudo chmod 644 /lib/systemd/system/myshutdown.service

sudo systemctl daemon-reload 
sudo systemctl enable myshutdown.service
Reboot the Pi and your custom service should run.

Check with:
sudo service myshutdown status (which should show the service as 'active (running)'). 

Now, when the Robosapien executes a 'Rosebud' shutdown command and the 'VRE' pin voltage (connected to GPIO 12) falls from 3.3v to 0v, 'Shutdown.py' will issue a 'sudo shutdown -h now' command, causing the Pi to shut down approximately 20 seconds later.
