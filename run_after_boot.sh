##! /bin/sh

# run from crontab 
# e.g.@reboot python /home/pi/MyScript.py &

sleep 5
/usr/local/bin/ngrok start --all \
  --config=/home/pi/.ngrok2/ngrok.yml \
  --log=stdout \
  > /home/pi/logs/ngrok.log &

/usr/bin/python /home/pi/dev/hue.py > /home/pi/logs/hue.log &
/usr/bin/python /home/pi/dev/dash.py > /home/pi/logs/dash.log &

