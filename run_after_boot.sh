##! /bin/sh

# run from crontab 
# e.g.@reboot python /home/pi/MyScript.py &

/usr/bin/python /home/pi/dev/alexa.py > /home/pi/logs/alexa.log &
/usr/bin/python /home/pi/dev/dash.py > /home/pi/logs/dash.log &
/usr/bin/python /home/pi/dev/webui.py > /home/pi/logs/webui.log &

sleep 10
/usr/local/bin/ngrok start --all \
  --config=/home/pi/.ngrok2/ngrok.yml \
  --log=stdout \
  > /home/pi/logs/ngrok.log &


