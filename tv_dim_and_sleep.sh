cd /home/pi/dev/BlackBeanControl
BBC=./BlackBeanControl.py

echo "Setting TV to night mode"
# appletv mode
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK

$BBC -c INPUT
$BBC -c LARROW
$BBC -c LARROW
$BBC -c RARROW
$BBC -c ENTER

$BBC -c QMENU
$BBC -c LARROW
$BBC -c LARROW
$BBC -c LARROW
$BBC -c LARROW
$BBC -c LARROW
$BBC -c LARROW
$BBC -c LARROW

# sleep timer
$BBC -c RARROW
$BBC -c RARROW
$BBC -c RARROW
$BBC -c ENTER
$BBC -c DARROW
$BBC -c DARROW
$BBC -c DARROW
$BBC -c DARROW
$BBC -c DARROW
$BBC -c ENTER

# energy
$BBC -c RARROW
$BBC -c ENTER
$BBC -c DARROW
$BBC -c DARROW
$BBC -c DARROW
$BBC -c ENTER

$BBC -c QMENU

$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK
$BBC -c BACK













