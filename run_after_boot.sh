##! /bin/sh

# run from crontab 
# e.g.@reboot python /home/pi/MyScript.py &

/usr/bin/python /home/pi/dev/alexa.py > /home/pi/logs/alexa.log &
/usr/bin/python /home/pi/dev/dash.py > /home/pi/logs/dash.log &
/usr/bin/python /home/pi/dev/webui.py > /home/pi/logs/webui.log &
/bin/sh /home/pi/dev/start_ngrok.sh &

