from src.connection import execute_command
execute_command('echo "Automation triggered from Windows" >> au.txt')
execute_command('DISPLAY=:0 notify-send "Automation" "Message from Windows"')


