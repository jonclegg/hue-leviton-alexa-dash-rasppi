This is an experimental project to control my Hue and Leviton lights using a raspberry pi 3. 

With this setup you can control your Hue and Leviton lights using an Alexa and an Amazon Dash button

Features:
* Control hue and Leviton dimmer with one Alexa command, currently 4 hard coded “scenes” are set.
* Control hue and Levitons scene from dash button

Setup:

1. ssh to the raspberry pi and make a */home/pi/dev* and */home/pi/logs* directories
2. run sudo *crontab -e* add a line like this
```
@reboot sh /home/pi/run_after_boot.sh > /home/pi/logs/cronlog &
```
3. create a file called config.py in ~/dev/
```
iftttBase = "https://maker.ifttt.com/trigger/<trigger_keyword>/with/key/<youiftttkey>"
hueBridgeIP = <ip_to_hue_bridge>
bountyMAC = <mac_address_for_dash_button>
```

You need to configure your [ifttt Webhook](https://ifttt.com/services/maker_webhooks/settings), then make a if->your Webhook and that->Leviton activity. You can configure an activity using the leviton app that will set the desired brightness. Give that a name. For example i have” table_16” to set my dinning room table to 16%.

run_after_boot.sh calls:
* ngrok - tool to setup a https tunnel from the outside world to the raspberry pi
* alexa.py - Alexa skill server using flask ask
* hue.py - Script to control hue and leviton lights — this in turn calls ifttt to control leviton.

4. You’ll also need to make an Alexa skill, here are the settings i used:
Invocation name: ‘berry’

```
{
  "intents": [
    {
      "slots": [
        {
          "name": "mode",
          "type": "LIST_OF_MODES"
        }
      ],
      "intent": "LightMode"
    }
  ]
}
```

Custom slot types called LIST_OF_MODES
```
tv
dim
bright
super bright
```

Sample Utterances:
```
LightMode to mode {mode}
LightMode be {mode}
LightMode to be {mode}
LightMode {mode}
```

6. Setup a ngrok basic account to have a static domain for the Alexa skill to reach your raspberry pi, set that as the https local for your Alexa skill

7. Before running hue.py, push the button on your Hue bridge to enable the configure mode. To find out the mac address of your dash run dash.py to have it print the mac address. Put that mac addr into the config.py.



